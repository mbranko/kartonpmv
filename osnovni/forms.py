#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import IntegerField, CharField, ModelChoiceField, DateField, Textarea, DateInput, HiddenInput, \
    ModelForm, Form
from osnovni.models import MuzejskiPredmet, VrstaZbirke, KategorijaPredmeta
from orgsema.models import NaseljenoMesto, Radnik


class PredmetForm(ModelForm):
    datum_nastanka = DateField(widget=DateInput(format='%d.%m.%Y.'), input_formats=('%d.%m.%Y.',), required=False)
    datum_kreiranja = DateField(widget=HiddenInput, input_formats=('%d.%m.%Y.', '%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d'))

    class Meta:
        model = MuzejskiPredmet
        fields = '__all__'
        widgets = {
            'opis': Textarea(attrs={'cols': 40, 'rows': 8}),
            'istorijat': Textarea(attrs={'cols': 40, 'rows': 8}),
            'literatura': Textarea(attrs={'cols': 40, 'rows': 8}),
        }


class PredmetSearchForm(Form):
    inv_br = IntegerField(label=u'inventarni broj', min_value=1, required=False)
    vrsta_predmeta = CharField(label=u'vrsta predmeta', required=False)
    vrsta_zbirke = ModelChoiceField(queryset=VrstaZbirke.objects.all(), label=u'vrsta zbirke', required=False)
    vreme_nastanka = CharField(label=u'vreme nastanka', required=False)
    datum_nastanka1 = DateField(widget=DateInput(format='%d.%m.%Y.'), input_formats=('%d.%m.%Y.',), label=u'datum nastanka od', required=False)
    datum_nastanka2 = DateField(widget=DateInput(format='%d.%m.%Y.'), input_formats=('%d.%m.%Y.',), label=u'do', required=False)
    mesto_nastanka = ModelChoiceField(queryset=NaseljenoMesto.objects.all(), label=u'mesto nastanka', required=False)
    opis = CharField(label=u'opis', required=False)
    autor = CharField(label=u'autor', required=False)
    kategorija = ModelChoiceField(queryset=KategorijaPredmeta.objects.all(), label=u'kategorija', required=False)
    obradio = CharField(label=u'predmet obradio', required=False)
    uneo = ModelChoiceField(queryset=Radnik.objects.all(), label=u'uneo', required=False)
    datum_unosa1 = DateField(widget=DateInput(format='%d.%m.%Y.'), input_formats=('%d.%m.%Y.',), label=u'datum unosa od', required=False)
    datum_unosa2 = DateField(widget=DateInput(format='%d.%m.%Y.'), input_formats=('%d.%m.%Y.',), label=u'do', required=False)

