# Generated by Django 2.1 on 2019-06-16 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiedotteet', '0004_auto_20190606_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='deadline_date',
            field=models.DateField(blank=True, default=datetime.date(2019, 6, 23), null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='end_date',
            field=models.DateField(default=datetime.date(2019, 6, 23)),
        ),
    ]