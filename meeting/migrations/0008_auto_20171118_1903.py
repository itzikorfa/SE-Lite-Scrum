# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-18 17:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0007_auto_20171118_1902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting',
            options={'ordering': ['-update']},
        ),
    ]
