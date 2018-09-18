# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-09 14:39
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_kulukorvaus', '0011_auto_20180906_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='KulukorvausPerustiedot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.CharField(max_length=50, verbose_name='Nimi')),
                ('email', models.EmailField(max_length=254, verbose_name='Sähköposti')),
                ('position_in_guild', models.CharField(choices=[('Hallitus', 'Hallitus'), ('Toimihenkilö', 'Toimihenkilö')], max_length=12, verbose_name='Asema killassa')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Puhelinnumero')),
                ('bank_number', models.CharField(max_length=32, verbose_name='Tilinumero (IBAN)')),
                ('bic', models.CharField(choices=[('OKOYFIHH', 'OKOYFIHH'), ('NDEAFIHH', 'NDEAFIHH'), ('SBANFIHH', 'SBANFIHH'), ('DABAFIHH', 'DABAFIHH'), ('HANDFIHH', 'HANDFIHH')], max_length=11, verbose_name='BIC')),
                ('sum_overall', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='korvaussumma yhteensä (euroa)')),
                ('additional_info', models.TextField(blank=True, verbose_name='Lisätietoja')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='kulukorvaukset/%Y-%m', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='PDF')),
                ('created_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'kulukorvaus perustiedot',
                'verbose_name_plural': 'Kulukorvaus perustiedot',
            },
        ),
        migrations.RemoveField(
            model_name='kulukorvauskulu',
            name='info',
        ),
        migrations.AlterModelOptions(
            name='kulukorvaus',
            options={'verbose_name': 'kulukorvaus', 'verbose_name_plural': 'Kulukorvaukset'},
        ),
        migrations.RemoveField(
            model_name='kulukorvaus',
            name='bank_number',
        ),
        migrations.RemoveField(
            model_name='kulukorvaus',
            name='bic',
        ),
        migrations.RemoveField(
            model_name='kulukorvaus',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='kulukorvaus',
            name='created_by_user',
        ),
        migrations.RemoveField(
            model_name='kulukorvaus',
            name='email',
        ),
        migrations.RemoveField(
            model_name='kulukorvaus',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='kulukorvaus',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='kulukorvaus',
            name='position_in_guild',
        ),
        migrations.RemoveField(
            model_name='kulukorvaus',
            name='sum_overall',
        ),
        migrations.AddField(
            model_name='kulukorvaus',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 9, 9, 14, 37, 58, 196326), verbose_name='Luotu'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kulukorvaus',
            name='explanation',
            field=models.CharField(default='jassoo', max_length=100, verbose_name='Tapahtuma / kulun kohde'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kulukorvaus',
            name='receipt',
            field=models.FileField(default=None, upload_to='kulukorvaukset/%Y-%m', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], verbose_name='Kuitti'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kulukorvaus',
            name='sum_euros',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Summa (euroa)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kulukorvaus',
            name='target',
            field=models.CharField(default='testi', max_length=50, verbose_name='Kulun selite'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kulukorvaus',
            name='additional_info',
            field=models.TextField(blank=True, verbose_name='Lisätietoja, kulujen perusteita'),
        ),
        migrations.AlterField(
            model_name='kulukorvaus',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='KulukorvausKulu',
        ),
        migrations.AddField(
            model_name='kulukorvaus',
            name='info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_kulukorvaus.KulukorvausPerustiedot'),
        ),
    ]