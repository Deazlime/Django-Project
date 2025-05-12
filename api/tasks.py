from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_task_update_email(task_id, user_email):
    subject = 'Обновление задачи'
    message = f'Задача с ID {task_id} была обновлена.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)