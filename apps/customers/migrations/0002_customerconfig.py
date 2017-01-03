# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-31 00:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_squashed_0015_customer_about_page_guide'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerConfig',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='customers.Customer')),
                ('enable_periodic_rank_email', models.BooleanField(default=False)),
                ('enable_clearbit', models.BooleanField(default=True)),
            ],
        ),
    ]
