# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-18 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vete', '0004_auto_20160816_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='propietario',
            name='signos_clinicos',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
