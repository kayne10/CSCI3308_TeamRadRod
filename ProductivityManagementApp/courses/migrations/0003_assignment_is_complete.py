# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-10-24 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20161024_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
