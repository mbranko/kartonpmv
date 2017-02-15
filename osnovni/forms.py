#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm, DateField, DateInput
from osnovni.models import MuzejskiPredmet


class PredmetForm(ModelForm):
    datum_nastanka = DateField(widget=DateInput(format='%d.%m.%Y.'), input_formats=('%d.%m.%Y.',), required=False)

    class Meta:
        model = MuzejskiPredmet
        fields = '__all__'
