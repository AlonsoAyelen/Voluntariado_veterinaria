# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-16 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vete', '0014_auto_20161116_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canino',
            name='T',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='canino',
            name='peso',
            field=models.FloatField(),
        ),
    ]
