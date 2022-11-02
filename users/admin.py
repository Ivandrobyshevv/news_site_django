from django.contrib import admin
from .models import User, Likes, Newsletter


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Пользователь"""
    list_display = ['username', 'email', 'is_staff']


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ("user", 'news', 'likes')


@admin.register(Newsletter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('user',)
