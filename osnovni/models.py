#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os.path
from django.db import models
from orgsema.models import NaseljenoMesto, Radnik


def get_path_fotografija(instance, filename):
    """
    Definiše lokaciju fajlova na disku za fotografije muzejskih predmeta.

    :param instance: opis muzejskog predmeta
    :param filename: ime uploadovanog fajla
    :return: putanja do fajla gde će fajl biti snimljen
    """
    return os.path.join('predmeti/predmet-%d/fotografije/%s' % (instance.inv_broj, filename))


class VrstaPredmeta(models.Model):
    """
    Vrsta predmeta: plakat, kostim, ...
    """
    naziv = models.CharField(u'naziv', max_length=100)
    aktivan = models.BooleanField(u'aktivan', default=True)

    def __unicode__(self):
        return self.naziv

    class Meta:
        verbose_name = u'vrsta predmeta'
        verbose_name_plural = u'vrste predmeta'


class VrstaZbirke(models.Model):
    """
    Vrsta zbirke: pozorišna, ...
    """
    naziv = models.CharField(u'naziv', max_length=100)
    aktivan = models.BooleanField(u'aktivan', default=True)

    def __unicode__(self):
        return self.naziv

    class Meta:
        verbose_name = u'vrsta zbirke'
        verbose_name_plural = u'vrste zbirke'


class NacinNabavke(models.Model):
    """
    Način nabavke: poklon, legat, ...
    """
    naziv = models.CharField(u'naziv', max_length=100)
    aktivan = models.BooleanField(u'aktivan', default=True)

    def __unicode__(self):
        return self.naziv

    class Meta:
        verbose_name = u'način nabavke'
        verbose_name_plural = u'načini nabavke'


class MuzejskiPredmet(models.Model):
    """
    Osnovni karton muzejskog predmeta
    """
    inv_broj = models.PositiveIntegerField(u'inventarni broj')
    br_mat_dok = models.CharField(u'broj matične dokumentacije', max_length=100, blank=True, null=True)
    vrsta_predmeta = models.ForeignKey(VrstaPredmeta, verbose_name=u'vrsta predmeta')
    vrsta_zbirke = models.ForeignKey(VrstaZbirke, verbose_name=u'vrsta zbirke')
    br_primeraka = models.PositiveIntegerField(u'broj primeraka')
    br_negativa = models.CharField(u'oznaka i broj negativa', max_length=200, blank=True, null=True)
    vreme_nastanka = models.CharField(u'vreme nastanka', max_length=100, blank=True, null=True)
    datum_nastanka = models.DateField(u'datum nastanka', blank=True, null=True)
    mesto_nastanka = models.CharField(u'mesto nastanka', max_length=200, blank=True, null=True)
    mesto_nastanka2 = models.ForeignKey(NaseljenoMesto, verbose_name=u'mesto nastanka', blank=True, null=True)
    autor = models.CharField(u'autor', max_length=200, blank=True, null=True)
    stil = models.CharField(u'stil, škola, radionica', max_length=1000, blank=True, null=True)
    materijal = models.CharField(u'materijal i tehnika', max_length=1000, blank=True, null=True)
    sirina = models.CharField(u'širina', max_length=20, blank=True, null=True)
    duzina = models.CharField(u'dužina', max_length=20, blank=True, null=True)
    visina = models.CharField(u'visina', max_length=20, blank=True, null=True)
    debljina = models.CharField(u'debljina', max_length=20, blank=True, null=True)
    precnik = models.CharField(u'prečnik', max_length=20, blank=True, null=True)
    grama = models.CharField(u'grama', max_length=20, blank=True, null=True)
    opis = models.CharField(u'opis', max_length=2000, blank=True, null=True)
    nacin_nabavke = models.ForeignKey(NacinNabavke, verbose_name=u'način nabavke', blank=True, null=True)
    opis_nabavke = models.CharField(u'opis nabavke', max_length=1000, blank=True, null=True)
    br_knjige_ulaza = models.PositiveIntegerField(u'broj knjige ulaza', blank=True, null=True)
    cena = models.CharField(u'cena', max_length=100, blank=True, null=True)
    kategorija = models.CharField(u'kategorija', max_length=100, blank=True, null=True)
    istorijat = models.CharField(u'istorijat', max_length=2000, blank=True, null=True)
    stanje_ocuvanosti = models.CharField(u'stanje i stepen očuvanosti', max_length=1000, blank=True, null=True)
    restauracija = models.CharField(u'restauracija i konzervacija', max_length=1000, blank=True, null=True)
    literatura = models.CharField(u'literatura o predmetu', max_length=2000, blank=True, null=True)
    smesten = models.CharField(u'smešten', max_length=1000, blank=True, null=True)
    obradio = models.CharField(u'predmet obradio', max_length=100, blank=True, null=True)
    napomena = models.CharField(u'napomena', max_length=2000, blank=True, null=True)
    fotografija = models.FileField(verbose_name=u'fotografija', upload_to=get_path_fotografija)

    def basepath(self):
        return os.path.basename(self.fotografija.name)

    def __unicode__(self):
        return str(self.inv_broj) + ": " + self.vrsta_predmeta.naziv

    class Meta:
        verbose_name = u'muzejski predmet'
        verbose_name_plural = u'muzejski predmeti'


class IstorijaIzmenaPredmeta(models.Model):
    """
    Istorija izmena u osnovnom kartonu muzejskog predmeta
    """
    predmet = models.ForeignKey(MuzejskiPredmet, verbose_name=u'predmet')
    radnik = models.ForeignKey(Radnik, verbose_name=u'radnik')
    timestamp = models.DateTimeField(u'vreme izmene')

    def __unicode__(self):
        return str(self.predmet.inv_broj) + ' / ' + self.radnik.puno_ime() + ' / ' + \
               self.timestamp.strftime('%d.%m.%Y. %H:%I:%S')

    class Meta:
        verbose_name = u'istorija izmena muzejskog predmeta'
        verbose_name_plural = u'istorije izmena muzejskih predmeta'
