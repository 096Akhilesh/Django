# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 06:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_clarifaimodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clarifaimodel',
            name='post',
        ),
        migrations.RemoveField(
            model_name='clarifaimodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='ClariFaiModel',
        ),
    ]
