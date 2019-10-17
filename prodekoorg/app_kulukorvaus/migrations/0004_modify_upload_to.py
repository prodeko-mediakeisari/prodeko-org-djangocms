# Generated by Django 2.2.5 on 2019-10-17 20:37

import django.core.validators
from django.db import migrations, models
import prodekoorg.app_kulukorvaus.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kulukorvaus', '0003_remove_kulukorvausperustiedot_position_in_guild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kulukorvaus',
            name='receipt',
            field=models.FileField(upload_to=prodekoorg.app_kulukorvaus.models.upload_url, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], verbose_name='Receipt'),
        ),
        migrations.AlterField(
            model_name='kulukorvausperustiedot',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=prodekoorg.app_kulukorvaus.models.upload_url, validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='PDF'),
        ),
    ]
