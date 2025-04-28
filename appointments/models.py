from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctors/', blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    symptoms = models.TextField()

    def __str__(self):
        return f'{self.patient} -> {self.doctor} on {self.appointment_date} at {self.appointment_time}'
