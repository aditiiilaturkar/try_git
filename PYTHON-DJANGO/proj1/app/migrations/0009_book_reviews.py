# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_issued_book_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reviews',
            field=models.CharField(default='aaa', max_length=100),
        ),
    ]