# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-21 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_cateringpackage_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='remarks',
            field=models.CharField(max_length=500, null=True),
        ),
    ]