# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-14 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0006_auto_20170521_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='cv',
            field=models.TextField(default='cv'),
        ),
    ]
