# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-26 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0106_remove_clientreference_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientreference',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
