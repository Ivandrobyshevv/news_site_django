from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import News, Categories


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


# Register your models here.

@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ['title', 'category', 'updated_at', 'is_published']
    form = NewsAdminForm
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Categories)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']
