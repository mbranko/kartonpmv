#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.utils.safestring import mark_safe
import django_tables2 as tables
from django_tables2.columns import LinkColumn, Column, DateTimeColumn, DateColumn
from django_tables2.utils import A
from osnovni.models import MuzejskiPredmet, IstorijaIzmenaPredmeta
from orgsema.models import Radnik


class PredmetList(tables.Table):
    class Meta:
        model = MuzejskiPredmet
        fields = ['inv_broj', 'vrsta_predmeta', 'vrsta_zbirke', 'datum_nastanka', 'opis', 'kreirao']
        attrs = {'class': 'table table-striped table-bordered table-hover'}

    inv_broj = LinkColumn('edit', args=[A('id')], verbose_name=mark_safe(u'Inv.br.'))


class RadniciList(tables.Table):
    class Meta:
        model = Radnik
        fields = ['puno_ime', 'br_kartona']
        attrs = {'class': 'table table-striped table-bordered table-hover'}

    puno_ime = Column(verbose_name='Radnik')
    br_kartona = Column(verbose_name='Br unetih kartona')


class PredmetHistoryList(tables.Table):
    class Meta:
        model = IstorijaIzmenaPredmeta
        fields = ['radnik', 'timestamp']
        attrs = {'class': 'table table-striped table-bordered table-hover'}

    timestamp = DateTimeColumn(format='d.m.Y. H:i')


class InvKnjiga(tables.Table):
    class Meta:
        model = MuzejskiPredmet
        fields = ['inv_broj', 'datum_kreiranja', 'br_knjige_ulaza', 'vrsta_zbirke', 'predmet_opis', 'materijal',
                  'autor_stil', 'mesto_vreme', 'dimenzije', 'istorijat', 'stanje_ocuvanosti', 'restauracija',
                  'br_negativa', 'opis_nabavke', 'cena', 'protokol_racun', 'napomena']
        attrs = {'class': 'table table-striped table-bordered table-hover'}

    inv_broj = Column(verbose_name='inv.br')
    datum_kreiranja = DateColumn(verbose_name='datum unosa', format='d.m.Y.')
    br_knjige_ulaza = Column(verbose_name='knjiga ulaza')
    vrsta_zbirke = Column(verbose_name='zbirka')
    predmet_opis = Column(verbose_name='predmet i opis')
    materijal = Column(verbose_name='materijal i tehnika')
    autor_stil = Column(verbose_name=u'autor, stil, škola, radionica')
    mesto_vreme = Column(verbose_name='mesto i vreme nastanka')
    dimenzije = Column(verbose_name='dimenzije')
    istorijat = Column(verbose_name='istorijat')
    stanje_ocuvanosti = Column(verbose_name='stanje predmeta')
    restauracija = Column(verbose_name='konzervacija, restauracija')
    br_negativa = Column(verbose_name='br. negativa')
    opis_nabavke = Column(verbose_name='podaci o darodavcu, prodavcu')
    cena = Column(verbose_name='nabavna cena')
    protokol_racun = Column(verbose_name=u'broj delovodnog protokola i računa')
    napomena = Column(verbose_name='napomena')



