# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-16 12:28
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('covey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='what todo')),
                ('priority', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('description', models.TextField(blank=True, default='')),
                ('estimated_time', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('ETA', models.DateField(blank=True, null=True)),
                ('presentage_complete', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='%completed')),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='assign at')),
                ('task_completed', models.BooleanField(default=False, verbose_name='completed')),
                ('task_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logcovmat', to='covey.CoveyMatrix')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['priority', 'timestamp'],
            },
        ),
        migrations.CreateModel(
            name='TodoLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField()),
                ('presentage_complete', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='%completed')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='log at')),
                ('update', models.DateTimeField(auto_now=True)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todolog', to='todo.Todo')),
            ],
        ),
    ]
