# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-15 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osnovni', '0002_auto_20170215_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muzejskipredmet',
            name='vrsta_predmeta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='osnovni.VrstaPredmeta', verbose_name='vrsta predmeta'),
        ),
        migrations.AlterField(
            model_name='muzejskipredmet',
            name='vrsta_zbirke',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='osnovni.VrstaZbirke', verbose_name='vrsta zbirke'),
        ),
    ]