from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", max_length=100)
    last_name = forms.CharField(label="Фамилия", max_length=100)
    phone_number = forms.CharField(label="Номер телефона", max_length=20)

    class Meta:
        model = Appointment
        fields = ['appointment_time', 'description']
