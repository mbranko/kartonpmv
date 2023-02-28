#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from django.contrib.auth.models import User
from django.db import models


def get_upload_path_avatar(instance, filename):
    return os.path.join('avatars/user-%d' % instance.id, filename)


class Valuta(models.Model):
    sifra = models.CharField(u'šifra', max_length=3)
    naziv = models.CharField(u'naziv', max_length=100)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name = u'valuta'
        verbose_name_plural = u'valute'


class Drzava(models.Model):
    sifra = models.CharField(u'šifra', max_length=2)
    naziv = models.CharField(u'naziv', max_length=100)
    valuta = models.ForeignKey(Valuta, verbose_name=u'valuta', on_delete=models.PROTECT)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name = u'država'
        verbose_name_plural = u'države'


class Region(models.Model):
    naziv = models.CharField(u'naziv', max_length=100)
    drzava = models.ForeignKey(Drzava, verbose_name=u'država', on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name = u'region'
        verbose_name_plural = u'regioni'


class Okrug(models.Model):
    sifra = models.CharField(u'šifra', max_length=2)
    naziv = models.CharField(u'naziv', max_length=100)
    region = models.ForeignKey(Region, verbose_name=u'region', on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name = u'okrug'
        verbose_name_plural = u'okruzi'


class Opstina(models.Model):
    naziv = models.CharField(u'naziv', max_length=100)
    okrug = models.ForeignKey(Okrug, verbose_name=u'okrug', on_delete=models.CASCADE)
    maticni_broj = models.CharField(u'matični broj', max_length=5)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name = u'opština'
        verbose_name_plural = u'opštine'


class NaseljenoMesto(models.Model):
    naziv = models.CharField(u'naziv', max_length=50)
    zip_code = models.CharField(u'poštanski broj', max_length=15)
    opstina = models.ForeignKey(Opstina, verbose_name=u'opština', on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name = u'naseljeno mesto'
        verbose_name_plural = u'naseljena mesta'


class OrgJed(models.Model):
    sifra = models.CharField(u'šifra', max_length=6)
    naziv = models.CharField(u'naziv', max_length=100)
    nadjed = models.ForeignKey('self', verbose_name=u'nadređena jedinica', blank=True, null=True, on_delete=models.CASCADE)
    nivo = models.PositiveSmallIntegerField(u'nivo', blank=True, null=True)
    mesto = models.ForeignKey(NaseljenoMesto, verbose_name=u'mesto', blank=True, null=True, on_delete=models.PROTECT)
    adresa = models.CharField(u'adresa', max_length=200, blank=True, null=True)
    email = models.CharField(u'email', max_length=200, blank=True, null=True)
    aktivna = models.BooleanField(u'aktivna', default=True)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name = u'organizaciona jedinica'
        verbose_name_plural = u'organizacione jedinice'


class Uloga(models.Model):
    naziv = models.CharField(u'naziv', max_length=100)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name = u'uloga'
        verbose_name_plural = u'uloge'


class Radnik(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.PROTECT)
    uloga = models.ForeignKey(Uloga, verbose_name=u'uloga', on_delete=models.PROTECT)
    orgjed = models.ForeignKey(OrgJed, verbose_name=u'organizaciona jedinica', on_delete=models.CASCADE)
    avatar = models.FileField(upload_to=get_upload_path_avatar, blank=True, null=True)

    def __str__(self):
        if self.user is None:
            return 'Nepoznato ime'
        return self.user.first_name + ' ' + self.user.last_name

    def puno_ime(self):
        if self.user is None:
            return 'Nepoznato ime'
        return self.user.first_name + ' ' + self.user.last_name

    def email(self):
        return self.user.email

    def username(self):
        return self.user.username

    def safe_avatar_url(self):
        if self.avatar.name:
            return self.avatar.url
        else:
            from kartonpmv import settings
            return settings.EMPTY_AVATAR_URL

    class Meta:
        verbose_name = u'radnik'
        verbose_name_plural = u'radnici'
        app_label = 'orgsema'  # za auth profil


