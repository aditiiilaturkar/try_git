# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180713_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='copies',
        ),
    ]