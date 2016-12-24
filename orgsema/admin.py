#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from orgsema.models import *


class NaseljenoMestoAdmin(admin.ModelAdmin):
    list_display = ('zip_code', 'naziv', 'opstina')
    ordering = ('naziv',)


class OpstinaAdmin(admin.ModelAdmin):
    list_display = ('naziv', 'okrug')
    ordering = ('naziv',)


class OkrugAdmin(admin.ModelAdmin):
    list_display = ('naziv', 'sifra', 'region')
    ordering = ('sifra',)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('naziv', 'drzava')
    ordering = ('drzava', 'naziv')


admin.site.register(Valuta)
admin.site.register(Drzava)
admin.site.register(Region, RegionAdmin)
admin.site.register(Okrug, OkrugAdmin)
admin.site.register(Opstina, OpstinaAdmin)
admin.site.register(NaseljenoMesto, NaseljenoMestoAdmin)
admin.site.register(OrgJed)
admin.site.register(Radnik)
