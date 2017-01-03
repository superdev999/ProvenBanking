# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0036_auto_20150522_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procurementcontact',
            name='user',
            field=models.OneToOneField(related_name='procurement_contacts', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='procurementcontact',
            name='vendors',
            field=models.ManyToManyField(related_name='procurement_contacts', null=True, to='vendors.Vendor', blank=True),
            preserve_default=True,
        ),
    ]
