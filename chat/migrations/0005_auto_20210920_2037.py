# Generated by Django 3.2.7 on 2021-09-20 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20210920_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delayedmessages',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 20, 37, 10, 510248), verbose_name='Date and time'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 20, 37, 10, 509247), verbose_name='Date and time'),
        ),
    ]
