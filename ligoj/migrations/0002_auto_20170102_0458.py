# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligoj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='status',
            field=models.CharField(choices=[('ACT', 'active'), ('HID', 'hidden')], default='ACT', max_length=3),
        ),
    ]
