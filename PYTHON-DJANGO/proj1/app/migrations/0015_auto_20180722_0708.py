# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-22 07:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20180722_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issued_book',
            name='issue_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 7, 22, 7, 8, 27, 30292)),
        ),
        migrations.AlterField(
            model_name='issued_book',
            name='return_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 6, 7, 8, 27, 30322)),
        ),
    ]