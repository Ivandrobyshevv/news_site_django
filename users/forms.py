from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from .models import User


class LoginForm(AuthenticationForm):
    """Авторизация"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "login"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "password"}))


class RegisterForm(UserCreationForm):
    """Регистрация"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "login"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "password"}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('interests',)
