# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-03 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20170903_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reserver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservers', to='home.UserProfileInfo'),
        ),
    ]