# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_cateringpackages_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='cateringpackages',
            name='capacity',
            field=models.PositiveIntegerField(default=50),
        ),
    ]