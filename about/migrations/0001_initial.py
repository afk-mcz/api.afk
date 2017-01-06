# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 22:52
from __future__ import unicode_literals

import about.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('name', models.CharField(max_length=140)),
                ('slug', models.SlugField(editable=False)),
                ('text', models.TextField()),
                ('dateCreated', models.DateField(auto_now_add=True)),
                ('dateUpdated', models.DateField(auto_now=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('publish', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=140)),
                ('caption', models.CharField(blank=True, max_length=140)),
                ('image', models.ImageField(upload_to=about.models.imageLocation)),
                ('dateCreated', models.DateField(auto_now_add=True)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.Entry')),
            ],
            options={
                'ordering': ['order', 'dateCreated'],
            },
        ),
    ]