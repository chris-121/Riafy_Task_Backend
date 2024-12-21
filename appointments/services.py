from rest_framework.exceptions import ValidationError
from .models import Appointment
from .serializers import AppointmentSerializer
from .common.slots import SLOTS


def get_all_available_slots(date):
    if not date:
        raise ValidationError("Date must be provided.")

    appointments = Appointment.objects.filter(date__date=date)
    booked_slots = appointments.values_list("slot", flat=True)
    available_slots = [slot for slot in SLOTS if slot not in booked_slots]

    return available_slots


def create_appointment(appointment):
    if not appointment or not isinstance(appointment, dict):
        raise ValidationError("Invalid data type. Expected a dictionary.")

    serializer = AppointmentSerializer(data=appointment)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    else:
        raise ValidationError(serializer.errors)
