from rest_framework.exceptions import ValidationError
from .models import Appointment
from .serializers import AppointmentSerializer


def get_all_appointments(date):
    appointments = Appointment.objects.filter(date__date=date)
    serializer = AppointmentSerializer(appointments, many=True)
    return serializer.data


def create_appointment(appointment):
    if not appointment or not isinstance(appointment, dict):
        raise ValidationError("Invalid data type. Expected a dictionary.")

    serializer = AppointmentSerializer(data=appointment)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    else:
        raise ValidationError(serializer.errors)
