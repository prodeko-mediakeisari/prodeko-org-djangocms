# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-20 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_vaalit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='virka',
            name='auth_prodeko_user',
        ),
    ]
