from django.contrib import admin
from .models import User, Likes, Newsletter, Feedback


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


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'message', 'create_at')
