from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from .models import User


class LoginForm(AuthenticationForm):
    """Авторизация"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "login"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "password"}))


class RegisterForm(UserCreationForm):
    """Регистрация"""

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "login"}),
            "password1": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "password"}),
            "password2": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "password"})
        }


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name")
        widgets = {
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'})
        }
