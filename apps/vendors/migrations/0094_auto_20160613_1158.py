# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0093_auto_20160611_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='diversity',
            field=models.ManyToManyField(blank=True, related_name='diversity', to='vendors.Diversity'),
        ),
    ]
