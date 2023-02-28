#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
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


class KategorijaPredmeta(models.Model):
    """
    Kategorije: I, II, III, IV, ...
    """
    naziv = models.CharField('naziv', max_length=100)
    aktivan = models.BooleanField('aktivan', default=True)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name = 'kategorija predmeta'
        verbose_name_plural = 'kategorije predmeta'


class VrstaZbirke(models.Model):
    """
    Vrsta zbirke: pozorišna, ...
    """
    naziv = models.CharField('naziv', max_length=100)
    aktivan = models.BooleanField('aktivan', default=True)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name = 'vrsta zbirke'
        verbose_name_plural = 'vrste zbirke'


class NacinNabavke(models.Model):
    """
    Način nabavke: poklon, legat, ...
    """
    naziv = models.CharField('naziv', max_length=100)
    aktivan = models.BooleanField('aktivan', default=True)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name = 'način nabavke'
        verbose_name_plural = 'načini nabavke'


class MuzejskiPredmet(models.Model):
    """
    Osnovni karton muzejskog predmeta
    """
    inv_broj = models.PositiveIntegerField('inventarni broj')
    br_mat_dok = models.CharField('broj matične dokumentacije', max_length=100, blank=True, null=True)
    vrsta_predmeta = models.CharField('predmet', max_length=200, blank=True, null=True)
    vrsta_zbirke = models.ForeignKey(VrstaZbirke, verbose_name='vrsta zbirke', blank=True, null=True, on_delete=models.PROTECT)
    br_primeraka = models.PositiveIntegerField('broj primeraka', blank=True, null=True)
    br_negativa = models.CharField('oznaka i broj negativa', max_length=200, blank=True, null=True)
    vreme_nastanka = models.CharField('vreme nastanka', max_length=100, blank=True, null=True)
    datum_nastanka = models.DateField('datum nastanka', blank=True, null=True)
    mesto_nastanka = models.CharField('mesto nastanka', max_length=200, blank=True, null=True)
    mesto_nastanka2 = models.ForeignKey(NaseljenoMesto, verbose_name='mesto nastanka', blank=True, null=True, on_delete=models.PROTECT)
    autor = models.CharField('autor', max_length=200, blank=True, null=True)
    stil = models.CharField('stil, škola, radionica', max_length=1000, blank=True, null=True)
    materijal = models.CharField('materijal i tehnika', max_length=1000, blank=True, null=True)
    sirina = models.CharField('širina', max_length=20, blank=True, null=True)
    duzina = models.CharField('dužina', max_length=20, blank=True, null=True)
    visina = models.CharField('visina', max_length=20, blank=True, null=True)
    debljina = models.CharField('debljina', max_length=20, blank=True, null=True)
    precnik = models.CharField('prečnik', max_length=20, blank=True, null=True)
    grama = models.CharField('grama', max_length=20, blank=True, null=True)
    opis = models.CharField('opis', max_length=2000, blank=True, null=True)
    nacin_nabavke = models.ForeignKey(NacinNabavke, verbose_name='način nabavke', blank=True, null=True, on_delete=models.PROTECT)
    opis_nabavke = models.CharField('opis nabavke', max_length=1000, blank=True, null=True)
    br_knjige_ulaza = models.PositiveIntegerField('broj knjige ulaza', blank=True, null=True)
    cena = models.CharField('cena', max_length=100, blank=True, null=True)
    kategorija = models.ForeignKey(KategorijaPredmeta, verbose_name='kategorija', blank=True, null=True, on_delete=models.PROTECT)
    istorijat = models.CharField('istorijat', max_length=2000, blank=True, null=True)
    stanje_ocuvanosti = models.CharField('stanje i stepen očuvanosti', max_length=1000, blank=True, null=True)
    restauracija = models.CharField('restauracija i konzervacija', max_length=1000, blank=True, null=True)
    literatura = models.CharField('literatura o predmet', max_length=2000, blank=True, null=True)
    smesten = models.CharField('smešten', max_length=1000, blank=True, null=True)
    obradio = models.CharField('predmet obradio', max_length=100, blank=True, null=True)
    napomena = models.CharField('napomena', max_length=2000, blank=True, null=True)
    br_protokola = models.CharField('broj delovodnog protokola', max_length=50, blank=True, null=True)
    br_racuna = models.CharField('broj računa', max_length=50, blank=True, null=True)
    datum_kreiranja = models.DateField('datum unosa')
    kreirao = models.ForeignKey(Radnik, verbose_name='zapis uneo', on_delete=models.PROTECT)
    fotografija = models.FileField(verbose_name='fotografija', upload_to=get_path_fotografija, blank=True, null=True)

    def basepath(self):
        return os.path.basename(self.fotografija.name)

    def __str__(self):
        return str(self.inv_broj) + ": " + self.vrsta_predmeta

    def predmet_opis(self):
        if self.vrsta_predmeta is not None and self.vrsta_predmeta != '':
            if self.opis is not None and self.opis != '':
                return self.vrsta_predmeta + ": " + self.opis
            else:
                return self.vrsta_predmeta
        else:
            if self.opis is not None and self.opis != '':
                return self.opis
            else:
                return ''

    def autor_stil(self):
        if self.autor is not None and self.autor != '':
            if self.stil is not None and self.stil != '':
                return self.autor + ": " + self.stil
            else:
                return self.autor
        else:
            if self.stil is not None and self.stil != '':
                return self.stil
            else:
                return ''

    def mesto_vreme(self):
        mesto = ''
        if self.mesto_nastanka is not None and self.mesto_nastanka != '':
            mesto = self.mesto_nastanka + ' '
        if self.mesto_nastanka2 is not None:
            mesto += '[' + self.mesto_nastanka2 + ']'
        vreme = ''
        if self.vreme_nastanka is not None and self.vreme_nastanka != '':
            vreme = self.vreme_nastanka + ' '
        if self.datum_nastanka is not None:
            vreme += datetime.date.strftime(self.datum_nastanka, '%d.%m.%Y.')
        return mesto + ' ' + vreme

    def dimenzije(self):
        dim = ''
        if self.sirina is not None and self.sirina != '':
            dim += ' š:[' + self.sirina + ']'
        if self.duzina is not None and self.duzina != '':
            dim += ' d:[' + self.duzina + ']'
        if self.visina is not None and self.visina != '':
            dim += ' v:[' + self.visina + ']'
        if self.debljina is not None and self.debljina != '':
            dim += ' b:[' + self.debljina + ']'
        if self.precnik is not None and self.precnik != '':
            dim += ' p:[' + self.precnik + ']'
        if self.grama is not None and self.grama != '':
            dim += ' g:[' + self.grama + ']'
        return dim

    def protokol_racun(self):
        if self.br_protokola is not None and self.br_protokola != '':
            if self.br_racuna is not None and self.br_racuna != '':
                return self.br_protokola + ": " + self.br_racuna
            else:
                return self.br_protokola
        else:
            if self.br_racuna is not None and self.br_racuna != '':
                return self.br_racuna
            else:
                return ''


    class Meta:
        verbose_name = 'muzejski predmet'
        verbose_name_plural = 'muzejski predmeti'


class IstorijaIzmenaPredmeta(models.Model):
    """
    Istorija izmena u osnovnom kartonu muzejskog predmeta
    """
    predmet = models.ForeignKey(MuzejskiPredmet, verbose_name='predmet', on_delete=models.CASCADE)
    radnik = models.ForeignKey(Radnik, verbose_name='radnik', on_delete=models.PROTECT)
    timestamp = models.DateTimeField('vreme izmene')

    def __str__(self):
        return str(self.predmet.inv_broj) + ' / ' + self.radnik.puno_ime() + ' / ' + \
               self.timestamp.strftime('%d.%m.%Y. %H:%I:%S')

    class Meta:
        verbose_name = 'istorija izmena muzejskog predmeta'
        verbose_name_plural = 'istorije izmena muzejskih predmeta'
