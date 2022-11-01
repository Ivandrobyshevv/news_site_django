from django import template
from users.models import Likes

register = template.Library()


@register.simple_tag(takes_context=True)
def is_liked(context, news_id):
    request = context['request']
    try:
        news_likes = Likes.objects.get(news_id=news_id, user=request.user.id).likes
    except Exception as e:
        news_likes = False
    return news_likes


@register.simple_tag()
def count_likes(news_id):
    return Likes.objects.filter(news_id=news_id, likes=True).count()


@register.simple_tag(takes_context=True)
def news_likes_id(context, news_id):
    request = context['request']
    return Likes.objects.get(news_id=news_id, user=request.user.id).id
