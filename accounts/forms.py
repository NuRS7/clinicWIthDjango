from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label="Аты")
    last_name = forms.CharField(max_length=100, required=True, label="Тегі")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
