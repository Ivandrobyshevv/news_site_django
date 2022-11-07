from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from .models import User, Feedback


class LoginForm(AuthenticationForm):
    """Авторизация"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "login"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "password"}))


class RegisterForm(UserCreationForm):
    """Регистрация"""
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Пароль"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Повторите пароль"}))

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")
        widgets = {
            "email": forms.EmailInput(attrs={"class": 'form-control', 'placeholder': "Email"}),
            "username": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Login"}),
        }


class UpdateUserForm(forms.ModelForm):
    """Обновление ифномрации пользователя"""

    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name")
        widgets = {
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'})
        }


class FeedbackForm(forms.ModelForm):
    """Форма отправки сообщения """

    class Meta:
        model = Feedback
        fields = ("email", "message")
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"rows": 5, "class": "form-control"})
        }
