# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-27 20:09
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_vaalit', '0007_auto_20180527_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ehdokas',
            name='introduction',
            field=ckeditor.fields.RichTextField(),
        ),
    ]