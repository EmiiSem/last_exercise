
from celery import shared_task
from django.core.mail import send_mail
from .models import Subscription  # Предположим, что у вас есть модель подписки
from celery import shared_task
from django.contrib.auth.models import User
from datetime import datetime, timedelta

@shared_task
def send_course_update_email(course_id, new_material):
    subscriptions = Subscription.objects.filter(course_id=course_id)
    course_name = "courses"
    subject = f"Обновление материалов курса {course_name}"
    message = f"Добавлен новый материал: {new_material}. Зайдите на сайт, чтобы просмотреть его."

    for subscription in subscriptions:
        send_mail(subject, message, 'from@example.com', [subscription.user.email])

@shared_task
def check_and_block_inactive_users():
    one_month_ago = datetime.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_active=True)

    for user in inactive_users:
        user.is_active = False
        user.save()
