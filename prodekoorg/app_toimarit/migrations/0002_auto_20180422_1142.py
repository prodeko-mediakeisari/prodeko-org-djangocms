# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-22 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_toimarit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toimari',
            name='puhelin',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='toimari',
            name='sahkoposti',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='toimari',
            name='virka_eng',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]