from django.db import models


class Appointment(models.Model):
    SLOT_CHOICES = [
        (10, "10:00 AM"),
        (10.5, "10:30 AM"),
        (11, "11:00 AM"),
        (11.5, "11:30 AM"),
        (12, "12:00 PM"),
        (12.5, "12:30 PM"),
        (2, "2:00 PM"),
        (2.5, "2:30 PM"),
        (3, "3:00 PM"),
        (3.5, "3:30 PM"),
        (4, "4:00 PM"),
        (4.5, "4:30 PM"),
    ]
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    date = models.DateTimeField("Appointment Date")
    slot = models.FloatField(choices=SLOT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
