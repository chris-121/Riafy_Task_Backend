from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    date = models.DateTimeField("Appointment Date")
    slot = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
