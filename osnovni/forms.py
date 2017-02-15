#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm
from osnovni.models import MuzejskiPredmet


class PredmetForm(ModelForm):
    class Meta:
        model = MuzejskiPredmet
        fields = '__all__'
