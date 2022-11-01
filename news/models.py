from django.db import models
from datetime import date
from django.urls import reverse


def get_upload_path(instance, filename):
    return f'photos/{date.today()}/{instance.title, filename}'


class News(models.Model):
    """Новости"""
    title = models.CharField("Заголовок", max_length=150)
    content = models.TextField("Контент", blank=True)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='Категория', related_name='news')
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    photo = models.ImageField("Фото", upload_to=get_upload_path)
    slug = models.SlugField("URL", max_length=150, unique=True)
    is_published = models.BooleanField("Черновик?", default=False)

    class Meta:
        db_table = "News"
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})


class Categories(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=50, unique=True)
    slug = models.SlugField("URL", max_length=50, unique=True)

    class Meta:
        db_table = "Categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


