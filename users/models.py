from django.db import models

from django.contrib.auth.models import AbstractUser
from news.models import News


class User(AbstractUser):
    interests = models.ManyToManyField(News, verbose_name='Заметки', default=None, related_name="news")



