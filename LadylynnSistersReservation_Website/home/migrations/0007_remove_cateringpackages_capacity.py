# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 12:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_cateringpackages_capacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cateringpackages',
            name='capacity',
        ),
    ]
