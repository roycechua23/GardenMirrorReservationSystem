# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-21 06:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170921_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cateringpackage',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.EventArea'),
        ),
    ]