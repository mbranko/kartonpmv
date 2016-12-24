# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 14:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orgsema.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drzava',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sifra', models.CharField(max_length=2, verbose_name='\u0161ifra')),
                ('naziv', models.CharField(max_length=100, verbose_name='naziv')),
            ],
            options={
                'verbose_name': 'dr\u017eava',
                'verbose_name_plural': 'dr\u017eave',
            },
        ),
        migrations.CreateModel(
            name='NaseljenoMesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=50, verbose_name='naziv')),
                ('zip_code', models.CharField(max_length=15, verbose_name='po\u0161tanski broj')),
            ],
            options={
                'verbose_name': 'naseljeno mesto',
                'verbose_name_plural': 'naseljena mesta',
            },
        ),
        migrations.CreateModel(
            name='Okrug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sifra', models.CharField(max_length=2, verbose_name='\u0161ifra')),
                ('naziv', models.CharField(max_length=100, verbose_name='naziv')),
            ],
            options={
                'verbose_name': 'okrug',
                'verbose_name_plural': 'okruzi',
            },
        ),
        migrations.CreateModel(
            name='Opstina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100, verbose_name='naziv')),
                ('maticni_broj', models.CharField(max_length=5, verbose_name='mati\u010dni broj')),
                ('okrug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgsema.Okrug', verbose_name='okrug')),
            ],
            options={
                'verbose_name': 'op\u0161tina',
                'verbose_name_plural': 'op\u0161tine',
            },
        ),
        migrations.CreateModel(
            name='OrgJed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sifra', models.CharField(max_length=6, verbose_name='\u0161ifra')),
                ('naziv', models.CharField(max_length=100, verbose_name='naziv')),
                ('nivo', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='nivo')),
                ('adresa', models.CharField(blank=True, max_length=200, null=True, verbose_name='adresa')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='email')),
                ('aktivna', models.BooleanField(default=True, verbose_name='aktivna')),
                ('mesto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgsema.NaseljenoMesto', verbose_name='mesto')),
                ('nadjed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgsema.OrgJed', verbose_name='nadre\u0111ena jedinica')),
            ],
            options={
                'verbose_name': 'organizaciona jedinica',
                'verbose_name_plural': 'oganizacione jedinice',
            },
        ),
        migrations.CreateModel(
            name='Radnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administracija', models.BooleanField(verbose_name='administracija')),
                ('izvestaji', models.BooleanField(verbose_name='izve\u0161taji')),
                ('avatar', models.FileField(blank=True, null=True, upload_to=orgsema.models.get_upload_path_avatar)),
                ('orgjed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgsema.OrgJed', verbose_name='organizaciona jedinica')),
            ],
            options={
                'verbose_name': 'radnik',
                'verbose_name_plural': 'radnici',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100, verbose_name='naziv')),
                ('drzava', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgsema.Drzava', verbose_name='dr\u017eava')),
            ],
            options={
                'verbose_name': 'region',
                'verbose_name_plural': 'regioni',
            },
        ),
        migrations.CreateModel(
            name='Uloga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100, verbose_name='naziv')),
            ],
            options={
                'verbose_name': 'uloga',
                'verbose_name_plural': 'uloge',
            },
        ),
        migrations.CreateModel(
            name='Valuta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sifra', models.CharField(max_length=3, verbose_name='\u0161ifra')),
                ('naziv', models.CharField(max_length=100, verbose_name='naziv')),
            ],
            options={
                'verbose_name': 'valuta',
                'verbose_name_plural': 'valute',
            },
        ),
        migrations.AddField(
            model_name='radnik',
            name='uloga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgsema.Uloga', verbose_name='uloga'),
        ),
        migrations.AddField(
            model_name='radnik',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='okrug',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgsema.Region', verbose_name='region'),
        ),
        migrations.AddField(
            model_name='naseljenomesto',
            name='opstina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgsema.Opstina', verbose_name='op\u0161tina'),
        ),
        migrations.AddField(
            model_name='drzava',
            name='valuta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgsema.Valuta', verbose_name='valuta'),
        ),
    ]
