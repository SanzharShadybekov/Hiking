from django.core.mail import send_mail

from shop.celery import app
# from .models import Contact
from .send_email import send

@app.task
def send_spam_email(user_email):
    send(user_email)

@app.task
def send_beat_email():
    send_mail(
        'Новый закаfffз',
        'Проверьте заказы',
        'johnsnowtest73@gmail.com',
        ['johnsnowtest73@gmail.com'],
        fail_silently=False,
        )