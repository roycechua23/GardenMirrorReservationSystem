# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-21 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20170921_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='remarks',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
