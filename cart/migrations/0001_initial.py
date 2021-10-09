# Generated by Django 3.2.6 on 2021-09-04 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('date', models.DateField(verbose_name='Дата доставки')),
                ('number', models.BigIntegerField(blank=True, null=True, verbose_name='Номер телефона получателя')),
                ('comments', models.CharField(blank=True, max_length=100, null=True, verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
