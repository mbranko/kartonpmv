# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-15 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import osnovni.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orgsema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IstorijaIzmenaPredmeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='vreme izmene')),
            ],
            options={
                'verbose_name': 'istorija izmena muzejskog predmeta',
                'verbose_name_plural': 'istorije izmena muzejskih predmeta',
            },
        ),
        migrations.CreateModel(
            name='MuzejskiPredmet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_broj', models.PositiveIntegerField(verbose_name='inventarni broj')),
                ('br_mat_dok', models.CharField(blank=True, max_length=100, null=True, verbose_name='broj mati\u010dne dokumentacije')),
                ('br_primeraka', models.PositiveIntegerField(verbose_name='broj primeraka')),
                ('br_negativa', models.CharField(blank=True, max_length=200, null=True, verbose_name='oznaka i broj negativa')),
                ('vreme_nastanka', models.CharField(blank=True, max_length=100, null=True, verbose_name='vreme nastanka')),
                ('datum_nastanka', models.DateField(blank=True, null=True, verbose_name='datum nastanka')),
                ('mesto_nastanka', models.CharField(blank=True, max_length=200, null=True, verbose_name='mesto nastanka')),
                ('autor', models.CharField(blank=True, max_length=200, null=True, verbose_name='autor')),
                ('stil', models.CharField(blank=True, max_length=1000, null=True, verbose_name='stil, \u0161kola, radionica')),
                ('materijal', models.CharField(blank=True, max_length=1000, null=True, verbose_name='materijal i tehnika')),
                ('sirina', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u0161irina')),
                ('duzina', models.CharField(blank=True, max_length=20, null=True, verbose_name='du\u017eina')),
                ('visina', models.CharField(blank=True, max_length=20, null=True, verbose_name='visina')),
                ('debljina', models.CharField(blank=True, max_length=20, null=True, verbose_name='debljina')),
                ('precnik', models.CharField(blank=True, max_length=20, null=True, verbose_name='pre\u010dnik')),
                ('grama', models.CharField(blank=True, max_length=20, null=True, verbose_name='grama')),
                ('opis', models.CharField(blank=True, max_length=2000, null=True, verbose_name='opis')),
                ('opis_nabavke', models.CharField(blank=True, max_length=1000, null=True, verbose_name='opis nabavke')),
                ('br_knjige_ulaza', models.PositiveIntegerField(blank=True, null=True, verbose_name='broj knjige ulaza')),
                ('cena', models.CharField(blank=True, max_length=100, null=True, verbose_name='cena')),
                ('kategorija', models.CharField(blank=True, max_length=100, null=True, verbose_name='kategorija')),
                ('istorijat', models.CharField(blank=True, max_length=2000, null=True, verbose_name='istorijat')),
                ('stanje_ocuvanosti', models.CharField(blank=True, max_length=1000, null=True, verbose_name='stanje i stepen o\u010duvanosti')),
                ('restauracija', models.CharField(blank=True, max_length=1000, null=True, verbose_name='restauracija i konzervacija')),
                ('literatura', models.CharField(blank=True, max_length=2000, null=True, verbose_name='literatura o predmetu')),
                ('smesten', models.CharField(blank=True, max_length=1000, null=True, verbose_name='sme\u0161ten')),
                ('obradio', models.CharField(blank=True, max_length=100, null=True, verbose_name='predmet obradio')),
                ('napomena', models.CharField(blank=True, max_length=2000, null=True, verbose_name='napomena')),
                ('fotografija', models.FileField(upload_to=osnovni.models.get_path_fotografija, verbose_name='fotografija')),
                ('mesto_nastanka2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgsema.NaseljenoMesto', verbose_name='mesto nastanka')),
            ],
            options={
                'verbose_name': 'muzejski predmet',
                'verbose_name_plural': 'muzejski predmeti',
            },
        ),
        migrations.CreateModel(
            name='NacinNabavke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100, verbose_name='naziv')),
                ('aktivan', models.BooleanField(default=True, verbose_name='aktivan')),
            ],
            options={
                'verbose_name': 'na\u010din nabavke',
                'verbose_name_plural': 'na\u010dini nabavke',
            },
        ),
        migrations.CreateModel(
            name='VrstaPredmeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100, verbose_name='naziv')),
                ('aktivan', models.BooleanField(default=True, verbose_name='aktivan')),
            ],
            options={
                'verbose_name': 'vrsta predmeta',
                'verbose_name_plural': 'vrste predmeta',
            },
        ),
        migrations.CreateModel(
            name='VrstaZbirke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100, verbose_name='naziv')),
                ('aktivan', models.BooleanField(default=True, verbose_name='aktivan')),
            ],
            options={
                'verbose_name': 'vrsta zbirke',
                'verbose_name_plural': 'vrste zbirke',
            },
        ),
        migrations.AddField(
            model_name='muzejskipredmet',
            name='nacin_nabavke',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='osnovni.NacinNabavke', verbose_name='na\u010din nabavke'),
        ),
        migrations.AddField(
            model_name='muzejskipredmet',
            name='vrsta_predmeta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osnovni.VrstaPredmeta', verbose_name='vrsta predmeta'),
        ),
        migrations.AddField(
            model_name='muzejskipredmet',
            name='vrsta_zbirke',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osnovni.VrstaZbirke', verbose_name='vrsta zbirke'),
        ),
        migrations.AddField(
            model_name='istorijaizmenapredmeta',
            name='predmet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osnovni.MuzejskiPredmet', verbose_name='predmet'),
        ),
        migrations.AddField(
            model_name='istorijaizmenapredmeta',
            name='radnik',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgsema.Radnik', verbose_name='radnik'),
        ),
    ]