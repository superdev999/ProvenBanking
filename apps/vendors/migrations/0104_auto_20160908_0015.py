# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-08 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0103_auto_20160906_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='sync_clearbit',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='score',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0),
        ),
    ]
