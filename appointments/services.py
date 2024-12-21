from django.shortcuts import get_object_or_404
from .models import Appointment
from .serializers import AppointmentSerializer


def get_all_appointments():
    todos = Appointment.objects.all()
    serializer = AppointmentSerializer(todos, many=True)
    return serializer.data
