# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0007_auto_20160128_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='name',
            field=models.CharField(blank=True, default=b'', max_length=127),
        ),
    ]
