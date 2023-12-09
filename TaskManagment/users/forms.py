from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Username:",
            "email": "Email:",
            "password1": "Password:",
            "password2": "Confirm your password:",
        }
        widgets = {
            "username": forms.TextInput(attrs={"class": "usernameInput"}),
            "email": forms.EmailInput(attrs={"class": "reg-email-input"}),
            "password": forms.PasswordInput(),
        }
