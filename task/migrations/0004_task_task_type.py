# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-14 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20171012_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.IntegerField(choices=[(1, 'important , urgent'), (2, 'important , not urgent'), (3, 'not important , urgent'), (4, 'not important , not urgent')], default=2),
        ),
    ]
