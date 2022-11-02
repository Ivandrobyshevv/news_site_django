from django.conf import settings

from news.models import Categories
from django.core.mail import send_mail
from django.template import loader


def send(user, categories_id: list):
    categories = Categories.objects.filter(id__in=categories_id)
    html_msg = loader.render_to_string('massage/message_1.html', context={"categories": categories, 'user': user})
    send_mail(
        'Подтверждение регистрации',  # Заголовок
        '',  # Текстовое тело, которое не нужно
        settings.EMAIL_HOST_USER,
        [user.email],
        html_message=html_msg,  # в html_message вставлять данные render_to_string
        fail_silently=False

    )
