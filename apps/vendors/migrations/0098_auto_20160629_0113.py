# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-29 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0097_vendorinvitation_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=254, verbose_name='Email'),
        ),
    ]