# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-18 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(editable=False),
        ),
    ]
