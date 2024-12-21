from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.utils import timezone
from .models import Appointment
from datetime import timedelta


class AppointmentTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.SLOTS = [10, 10.5, 11, 11.5, 12, 12.5, 2, 2.5, 3, 3.5, 4, 4.5]

        # Create a few appointments for testing
        self.appointment_1 = Appointment.objects.create(
            name="John Doe",
            phone_number="1234567890",
            date=timezone.now().isoformat(),
            slot=10,
        )
        self.appointment_2 = Appointment.objects.create(
            name="Jane Doe",
            phone_number="9876543210",
            date=timezone.now().isoformat(),
            slot=11,
        )

    def test_get_all_available_slots(self):
        # Test if available slots are returned correctly
        date = timezone.now().date()
        response = self.client.get(f"/api/v1/appointments?date={date}")

        # List of slots that are not booked
        booked_slots = [self.appointment_1.slot, self.appointment_2.slot]
        expected_available_slots = [
            slot for slot in self.SLOTS if slot not in booked_slots
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_available_slots)

    def test_get_all_available_slots_invalid_date_format(self):
        # Pass an invalid date format
        invalid_date = "2024-31-12"
        response = self.client.get(f"/api/v1/appointments?date={invalid_date}")

        # The response should be a 400 Bad Request with a validation error message
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_available_slots_past_date(self):
        # Test that an error is raised when a past date is provided
        past_date = timezone.now().date() - timezone.timedelta(days=1)

        # Request available slots for the past date
        response = self.client.get(f"/api/v1/appointments?date={past_date}")

        # Check if the response is a 400 error and the message is correct
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "Appointments cannot be made for past dates.", response.data["Error"]
        )

    def test_create_appointment_success(self):
        # Test creating an appointment successfully
        data = {
            "name": "Alice",
            "phone_number": "5555555555",
            "date": timezone.now().date().isoformat(),
            "slot": 12,
        }

        response = self.client.post("/api/v1/appointments", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Alice")
        self.assertEqual(response.data["slot"], 12)

    def test_create_appointment_slot_already_taken(self):
        # Test creating an appointment where the slot is already booked
        data = {
            "name": "Bob",
            "phone_number": "6666666666",
            "date": timezone.now().date().isoformat(),
            "slot": 10,
        }

        response = self.client.post("/api/v1/appointments", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Slot 10 on", response.data["Error"])

    def test_create_appointment_missing_date(self):
        # Test creating an appointment with missing date
        data = {"name": "Charlie", "phone_number": "7777777777", "slot": 10}

        response = self.client.post("/api/v1/appointments", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Both date and slot must be provided.", response.data["Error"])

    def test_create_appointment_missing_slot(self):
        # Test creating an appointment with missing slot
        data = {
            "name": "David",
            "phone_number": "8888888888",
            "date": timezone.now()
            .replace(hour=10, minute=0, second=0, microsecond=0)
            .isoformat(),
        }

        response = self.client.post("/api/v1/appointments", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Both date and slot must be provided.", response.data["Error"])
