#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from osnovni.forms import PredmetForm
from osnovni.models import *


@login_required
def index(request):
    return render(request, 'osnovni/index.html')


@login_required
def novi_predmet(request):
    if request.method == 'POST':
        form = PredmetForm(request.POST, request.FILES)
        if form.is_valid():
            pred = form.save()
            ist = IstorijaIzmenaPredmeta()
            ist.predmet = pred
            ist.radnik = request.user.radnik
            ist.timestamp = datetime.now()
            ist.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = PredmetForm(initial={'kreirao': request.user.radnik, 'datum_kreiranja': datetime.now()})
    context = {'form': form,
               'pagetitle': u'Novi karton',
               'maintitle': u'Novi karton',
               'titleinfo': u'Kreiranje novog kartona'}
    return render(request, 'osnovni/predmet.html', context)


@login_required
def predmet(request, predmet_id):
    try:
        pred = MuzejskiPredmet.objects.get(pk=predmet_id)
    except MuzejskiPredmet.DoesNotExist:
        return redirect('index')
    if request.method == 'POST':
        form = PredmetForm(request.POST, request.FILES, instance=pred)
        if form.is_valid():
            pred = form.save()
            ist = IstorijaIzmenaPredmeta()
            ist.predmet = pred
            ist.radnik = request.user.radnik
            ist.timestamp = datetime.now()
            ist.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = PredmetForm(instance=pred)
    context = {'form': form,
               'pagetitle': u'Pregled kartona',
               'maintitle': u'Pregled kartona',
               'titleinfo': u'Pregled i izmena podataka u kartonu br. ' + str(pred.inv_broj)}
    return render(request, 'osnovni/predmet.html', context)


@login_required
def pretraga(request):
    if request.method == 'POST':
        form = PredmetForm(request.POST)
        print form.cleaned_data
    else:
        form = PredmetForm()
    context = {'form': form,
               'pagetitle': u'Pretraga kartona',
               'maintitle': u'Pretraga kartona',
               'titleinfo': u'Unesite poznate podatke'}
    return render(request, 'osnovni/predmet.html', context)
