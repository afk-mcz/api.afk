# Generated by Django 2.0.5 on 2018-06-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0022_auto_20180621_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
