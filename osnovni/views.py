#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from dateutil import relativedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q, Count
from django_tables2 import RequestConfig

from osnovni.forms import PredmetForm, PredmetSearchForm
from osnovni.models import *
from osnovni.tables import *


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
            ist.timestamp = datetime.datetime.now()
            ist.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = PredmetForm(initial={'kreirao': request.user.radnik, 'datum_kreiranja': datetime.date.today()})
    context = {'form': form,
               'pagetitle': u'Novi karton',
               'maintitle': u'Novi karton',
               'titleinfo': u'Kreiranje novog kartona',
               'form_mode': 'new'}
    return render(request, 'osnovni/predmet.html', context)


@login_required
def predmet(request, predmet_id):
    try:
        pred = MuzejskiPredmet.objects.get(pk=predmet_id)
    except MuzejskiPredmet.DoesNotExist:
        return redirect('index')

    template = 'osnovni/predmet.html'
    context = {}
    context['pagetitle'] = u'Pregled kartona'
    context['maintitle'] = u'Pregled kartona'
    context['titleinfo'] = u'Pregled podataka u kartonu inv.br. ' + str(pred.inv_broj)
    context['form_mode'] = 'edit'

    if request.method == 'POST':
        form = PredmetForm(request.POST, request.FILES, instance=pred)
        if form.is_valid():
            pred = form.save()
            ist = IstorijaIzmenaPredmeta()
            ist.predmet = pred
            ist.radnik = request.user.radnik
            ist.timestamp = datetime.datetime.now()
            ist.save()
            return redirect('index')
        else:
            print(form.errors)

    else:
        form = PredmetForm(instance=pred)
        if request.user.radnik.uloga.id > 2:
            context['predmet'] = pred
            context['titleinfo'] = u'Pregled podataka u kartonu inv.br. ' + str(pred.inv_broj)
            template = 'osnovni/predmet_view.html'

    istorija = IstorijaIzmenaPredmeta.objects.filter(predmet=pred).order_by('timestamp')
    table = PredmetHistoryList(istorija)
    RequestConfig(request, paginate={'per_page': 20}).configure(table)
    context['form'] = form
    context['table'] = table
    return render(request, template, context)


@login_required
def pretraga(request):
    if request.method == 'POST':
        form = PredmetSearchForm(request.POST)
        if form.is_valid():
            query = None
            query_desc = ''

            inv_br = form.cleaned_data['inv_br']
            if inv_br is not None and inv_br != '':
                q = Q(inv_broj=inv_br)
                query = query & q if query is not None else q
                query_desc += ' inv.br:' + str(inv_br)

            vrsta_predmeta = form.cleaned_data['vrsta_predmeta']
            if vrsta_predmeta is not None and vrsta_predmeta != '':
                q = Q(vrsta_predmeta__icontains=vrsta_predmeta)
                query = query & q if query is not None else q
                query_desc += ' predmet:' + vrsta_predmeta

            vrsta_zbirke = form.cleaned_data['vrsta_zbirke']
            if vrsta_zbirke is not None:
                q = Q(vrsta_zbirke_id=vrsta_zbirke.id)
                query = query & q if query is not None else q
                query_desc += ' zbirka:' + vrsta_zbirke.naziv

            vreme_nastanka = form.cleaned_data['vreme_nastanka']
            if vreme_nastanka is not None and vreme_nastanka != '':
                q = Q(vreme_nastanka__icontains=vreme_nastanka)
                query = query & q if query is not None else q
                query_desc += ' vreme:' + vreme_nastanka

            datum_nastanka1 = form.cleaned_data['datum_nastanka1']
            if datum_nastanka1 is not None:
                q = Q(datum_nastanka__gte=datum_nastanka1)
                query = query & q if query is not None else q
                query_desc += ' od:' + datetime.date.strftime(datum_nastanka1, '%d.%m.%Y.')

            datum_nastanka2 = form.cleaned_data['datum_nastanka2']
            if datum_nastanka2 is not None:
                q = Q(datum_nastanka__lte=datum_nastanka2)
                query = query & q if query is not None else q
                query_desc += ' do:' + datetime.date.strftime(datum_nastanka2, '%d.%m.%Y.')

            mesto_nastanka = form.cleaned_data['mesto_nastanka']
            if mesto_nastanka is not None:
                q = Q(mesto_nastanka2=mesto_nastanka)
                query = query & q if query is not None else q
                query_desc += ' mesto:' + mesto_nastanka.naziv

            autor = form.cleaned_data['autor']
            if autor is not None and autor != '':
                q = Q(autor__icontains=autor)
                query = query & q if query is not None else q
                query_desc += ' autor:' + autor

            opis = form.cleaned_data['opis']
            if opis is not None and opis != '':
                q = Q(opis__icontains=opis)
                query = query & q if query is not None else q
                query_desc += ' opis:' + opis

            kategorija = form.cleaned_data['kategorija']
            if kategorija is not None:
                q = Q(kategorija=kategorija)
                query = query & q if query is not None else q
                query_desc += ' kat:' + kategorija.naziv

            obradio = form.cleaned_data['obradio']
            if obradio is not None and obradio != '':
                q = Q(obradio__icontains=obradio)
                query = query & q if query is not None else q
                query_desc += ' obradio:' + obradio

            uneo = form.cleaned_data['uneo']
            if uneo is not None:
                q = Q(kreirao=uneo)
                query = query & q if query is not None else q
                query_desc += ' uneo:' + uneo.puno_ime()

            datum_unosa1 = form.cleaned_data['datum_unosa1']
            if datum_unosa1 is not None:
                q = Q(datum_kreiranja__gte=datum_unosa1)
                query = query & q if query is not None else q
                query_desc += ' unos_od:' + datetime.date.strftime(datum_unosa1, '%d.%m.%Y.')

            datum_unosa2 = form.cleaned_data['datum_unosa2']
            if datum_unosa2 is not None:
                q = Q(datum_kreiranja__lte=datum_unosa2)
                query = query & q if query is not None else q
                query_desc += ' unos_do:' + datetime.date.strftime(datum_unosa2, '%d.%m.%Y.')

            if query is None:
                predmeti = MuzejskiPredmet.objects.all()
            else:
                predmeti = MuzejskiPredmet.objects.filter(query).distinct()
            return _prikazi_predmete(request, predmeti, u'Pretraga kartona', u'Rezultati pretrage', query_desc)
    else:
        form = PredmetSearchForm()
    context = {'form': form,
               'pagetitle': u'Pretraga kartona',
               'maintitle': u'Pretraga kartona',
               'titleinfo': u'Unesite poznate podatke'}
    return render(request, 'osnovni/pretraga.html', context)


@login_required
def moji_predmeti(request):
    predmeti = MuzejskiPredmet.objects.filter(kreirao=request.user.radnik)
    return _prikazi_predmete(request, predmeti, u'Moji kartoni', u'Moji kartoni', u'korisnika ' + request.user.username)


def _prikazi_predmete(request, predmeti, pagetitle, maintitle, titleinfo):
    table = PredmetList(predmeti)
    RequestConfig(request, paginate={'per_page': 20}).configure(table)
    context = {'table': table,
               'pagetitle': pagetitle,
               'maintitle': maintitle,
               'titleinfo': titleinfo}
    return render(request, 'osnovni/predmet_list.html', context)


@login_required
def statistika_unosa(request):
    danas = datetime.date.today()
    minus6 = danas - relativedelta.relativedelta(months=6)
    radnici = Radnik.objects.annotate(br_kartona=Count('muzejskipredmet')).\
        filter(muzejskipredmet__datum_kreiranja__gte=minus6).\
        filter(muzejskipredmet__datum_kreiranja__lte=danas)
    table = RadniciList(radnici)
    RequestConfig(request, paginate={'per_page': 20}).configure(table)
    context = {
        'table': table,
        'pagetitle': u'Statistika unosa',
        'maintitle': u'Statistika unosa',
        'titleinfo': u'za period od ' + datetime.date.strftime(minus6, '%d.%m.%Y.') + u' do ' +
                     datetime.date.strftime(danas, '%d.%m.%Y.')
    }
    return render(request, 'osnovni/statistika_unosa.html', context)
