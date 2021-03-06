# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20160121_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='links',
            field=models.ManyToManyField(to='portfolio.Link'),
        ),
        migrations.AddField(
            model_name='video',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='order',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
    ]
