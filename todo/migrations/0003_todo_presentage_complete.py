# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-14 18:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20171014_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='presentage_complete',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='%completed'),
        ),
    ]
