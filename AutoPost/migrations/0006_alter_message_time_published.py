# Generated by Django 4.0.1 on 2022-02-06 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoPost', '0005_alter_message_time_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time_published',
            field=models.TimeField(default=datetime.time(11, 13, 27, 625929)),
        ),
    ]
