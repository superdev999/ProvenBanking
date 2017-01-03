# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 14:35
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0004_auto_20150321_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', unique=True),
        ),
    ]
