# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-04 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ligoj', '0005_auto_20170104_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='name',
        ),
    ]
