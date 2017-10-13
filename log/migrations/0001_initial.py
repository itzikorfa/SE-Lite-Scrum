# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-08 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0003_auto_20171008_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField()),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log4tasks', to='task.TaskProperty')),
            ],
        ),
    ]