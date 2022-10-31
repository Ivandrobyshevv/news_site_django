from django import template
from news.models import Categories, News

register = template.Library()


@register.simple_tag
def get_categories():
    """категории"""
    return Categories.objects.all()


@register.simple_tag
def new_news():
    """5 последних опубликованных новостей"""
    return News.objects.filter(is_published=False)[:5]


