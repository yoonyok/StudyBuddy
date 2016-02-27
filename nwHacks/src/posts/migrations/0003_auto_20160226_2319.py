# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20160218_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preferred_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
            preserve_default=False,
        ),
    ]
