# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-25 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vete', '0008_auto_20160831_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propietario',
            name='ultima_inundacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
