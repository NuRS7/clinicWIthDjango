from django.db import models
from django.conf import settings

from django.db import models
from django.conf import settings

class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='doctors/')
    achievements = models.TextField(default='Нет достижений')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} — {self.specialization.name}"


class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    description = models.TextField(default="Проверка")

    def __str__(self):
        return f"Запись: {self.patient} к {self.doctor} на {self.appointment_time} {self.description}"
