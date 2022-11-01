from django.db import models

from django.contrib.auth.models import AbstractUser
from news.models import News


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
