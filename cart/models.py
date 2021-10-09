from django.db import models
from django.utils.translation import gettext as _


class Order(models.Model):
    first_name = models.CharField(_('Имя'), max_length=50)
    last_name = models.CharField(_('Фамилия'), max_length=50)
    email = models.EmailField(_('Электронная почта'),)
    address = models.CharField(_('Адрес'), max_length=150)
    date = models.DateField(_('Дата доставки'))
    number = models.BigIntegerField(_('Номер телефона получателя'), blank=True, null=True)
    comments = models.CharField(_('Комментарий'), max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"