# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-21 05:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CateringPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pax', models.PositiveIntegerField(default=50)),
                ('description', models.CharField(max_length=256)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EventArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='<django.db.models.fields.related.ForeignKey> event', max_length=100)),
                ('foodselections', models.CharField(default="GM's Choice", max_length=1000)),
                ('event_type', models.CharField(max_length=100)),
                ('currentdate', models.DateTimeField(auto_now=True)),
                ('event_date', models.DateField()),
                ('event_timestart', models.TimeField()),
                ('event_timeend', models.TimeField()),
                ('status', models.BooleanField(default=False)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package', to='home.CateringPackage')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=15)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='reserver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserver', to='home.UserProfileInfo'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='venue',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='eventarea', to='home.EventArea'),
        ),
    ]
