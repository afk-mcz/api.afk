# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
