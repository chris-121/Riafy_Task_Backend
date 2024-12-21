from rest_framework.exceptions import ValidationError
from .models import Appointment
from .serializers import AppointmentSerializer
from .common.slots import SLOTS
from django.utils import timezone
from datetime import datetime


def get_all_available_slots(date):
    if not date:
        raise ValidationError("Date must be provided.")

    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValidationError("Invalid date format. It must be in YYYY-MM-DD format.")

    if parsed_date < timezone.localdate():
        raise ValidationError("Appointments cannot be made for past dates.")

    appointments = Appointment.objects.filter(date__date=parsed_date)
    booked_slots = appointments.values_list("slot", flat=True)
    available_slots = [slot for slot in SLOTS if slot not in booked_slots]

    return available_slots


def create_appointment(appointment):
    print(appointment)
    if not appointment or not isinstance(appointment, dict):
        raise ValidationError("Invalid data type. Expected a dictionary.")

    date = appointment.get("date")
    slot = appointment.get("slot")

    # Ensure date and slot are provided
    if not date or not slot:
        raise ValidationError("Both date and slot must be provided.")

    # Check if the slot already exists for the given date
    if Appointment.objects.filter(date__date=date, slot=slot).exists():
        raise ValidationError(f"Slot {slot} on {date} is already taken.")

    serializer = AppointmentSerializer(data=appointment)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    else:
        raise ValidationError(serializer.errors)
