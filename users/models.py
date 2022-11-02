from django.db import models

from django.contrib.auth.models import AbstractUser
from news.models import News, Categories


class User(AbstractUser):
    interests = models.ManyToManyField(News, verbose_name='Заметки', default=None, related_name="news")


class Likes(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователи', on_delete=models.SET_NULL, null=True)
    news = models.ForeignKey(News, on_delete=models.SET_NULL, verbose_name="Новость", null=True)
    likes = models.BooleanField("like", default=False)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"


class Newsletter(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователе", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categories, verbose_name="Категории")
    create_at = models.DateTimeField("Дата подписки", auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.categories}'

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылка"
