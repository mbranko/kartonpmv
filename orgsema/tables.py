#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.utils.safestring import mark_safe
from django_tables2.columns import Column, BooleanColumn, EmailColumn
import django_tables2 as tables
from orgsema.models import Radnik


class ListaRadnika(tables.Table):
    id = Column(verbose_name=mark_safe('ID'))
    puno_ime = Column(verbose_name=mark_safe('Ime i prezime'))
    username = Column(verbose_name=mark_safe('Nalog'))
    email = EmailColumn(verbose_name=mark_safe('Email'))
    orgjed = Column(verbose_name=mark_safe('Org. jedinica'))
    uloga = Column(verbose_name=mark_safe('Uloga'))

    def __init__(self, *args, **kwargs):
        super(ListaRadnika, self).__init__(*args, **kwargs)

    def render_email(self, record):
        return record.user.email

    def render_orgjed(self, record):
        return record.orgjed.naziv

    def render_username(self, record):
        return record.user.username

    class Meta:
        model = Radnik
        attrs = {'class': 'table table-striped table-bordered table-hover'}
        fields = ('id', 'puno_ime', 'username', 'email', 'orgjed', 'uloga')
