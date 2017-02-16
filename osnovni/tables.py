#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.utils.safestring import mark_safe
import django_tables2 as tables
from django_tables2.columns import LinkColumn, Column, DateTimeColumn
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
