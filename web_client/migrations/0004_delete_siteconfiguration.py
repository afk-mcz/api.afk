# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-09 23:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0003_siteconfiguration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SiteConfiguration',
        ),
    ]
