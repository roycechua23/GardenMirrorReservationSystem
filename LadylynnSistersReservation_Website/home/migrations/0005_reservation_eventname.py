# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_cateringpackages_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='eventname',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]