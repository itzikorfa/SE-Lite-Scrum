# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-16 12:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 16, 12, 32, 7, 357032, tzinfo=utc)),
        ),
    ]
