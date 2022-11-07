import datetime

from celery import shared_task
from celery.schedules import crontab

from django.conf import settings
from django.core.mail import send_mail
from django.template import loader

from news.models import Categories, News
from users.models import Newsletter


@shared_task()
def send_feedback_email_task(email_address, message):
    """Отправляет электронное письмо после отправки формы обратной связи."""
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email_address],
        fail_silently=False
    )


@shared_task()
def send_category_subscription(email_address, categories_id, title="Подписка на рассылку"):
    """Подписка на категории"""
    categories = Categories.objects.filter(id__in=categories_id)
    msg_html = loader.render_to_string('massage/message_1.html', context={"categories": categories})

    send_mail(
        title,
        '',
        settings.EMAIL_HOST_USER,
        [email_address],
        html_message=msg_html,
        fail_silently=False
    )


@shared_task
def send_new_news_post():
    """Отправка новых новостей ежедневно в 20:00 """
    list_email, list_news = get_email_list_and_news_queryset()
    if not len(list_email) > 1:
        msg_html = loader.render_to_string('massage/message_2.html', context={'list_news': list_news})
        send_mail(
            "Новые новости",
            '',
            settings.EMAIL_HOST_USER,
            list_email,
            html_message=msg_html,
            fail_silently=False
        )
    else:
        for email, news in zip(list_email, list_news):
            msg_html = loader.render_to_string('massage/message_2.html', context={'list_news': news})
            send_mail(
                "Новые новости",
                '',
                settings.EMAIL_HOST_USER,
                recipient_list=[email],
                html_message=msg_html,
                fail_silently=False
            )


def get_email_list_and_news_queryset():
    user_list = [obj for obj in Newsletter.objects.all()]

    news_queryset = list()
    user_email_list = list()
    for user in user_list:
        news_queryset.append(News.objects.filter(created_at__day=datetime.date.today().day,
                                                 category_id__in=user.categories.all().values_list('id')))
        user_email_list.append(user.user.email)

    return user_email_list, news_queryset
