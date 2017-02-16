#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.utils.safestring import mark_safe
import django_tables2 as tables
from django_tables2.columns import LinkColumn
from django_tables2.utils import A
from osnovni.models import MuzejskiPredmet


class PredmetList(tables.Table):
    class Meta:
        model = MuzejskiPredmet
        fields = ['inv_broj', 'vrsta_predmeta', 'vrsta_zbirke', 'datum_nastanka', 'opis', 'kreirao']
        attrs = {'class': 'table table-striped table-bordered table-hover'}

    inv_broj = LinkColumn('edit', args=[A('id')], verbose_name=mark_safe(u'Inv.br.'))

