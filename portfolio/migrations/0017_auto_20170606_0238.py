# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 02:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20170519_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.LinkCategory'),
        ),
    ]
