from django.core.mail import send_mail


def send(user_email):
    send_mail(
        f'Новый заказ',
        'Проверьте заказы',
        'johnsnowtest73@gmail.com',
        ['johnsnowtest73@gmail.com'],
        fail_silently=False,
        )