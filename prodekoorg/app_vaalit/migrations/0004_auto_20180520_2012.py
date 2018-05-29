# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-20 20:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_vaalit', '0003_auto_20180520_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ehdokas',
            name='auth_prodeko_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ehdokkaat', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ehdokas',
            name='pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
