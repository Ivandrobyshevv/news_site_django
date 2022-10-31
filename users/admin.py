from django.contrib import admin
from .models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Пользователь"""
    list_display = ['username', 'email', 'is_staff']
