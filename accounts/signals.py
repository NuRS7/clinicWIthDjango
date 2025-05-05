from django.db.models.signals import post_save
from django.dispatch import receiver
from appointments.models import Patient
from .models import User
@receiver(post_save, sender=User)
def create_patient_profile(sender, instance, created, **kwargs):
    if created and instance.is_patient:
        Patient.objects.create(user=instance)
