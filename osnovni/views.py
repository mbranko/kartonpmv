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
        form = PredmetForm()
    context = {'form': form}
    return render(request, 'osnovni/predmet.html', context)


@login_required
def predmet(request, predmet_id):
    try:
        pred = MuzejskiPredmet.objects.get(pk=predmet_id)
    except MuzejskiPredmet.DoesNotExist:
        return redirect('index')
    if request.method == 'POST':
        form = PredmetForm(request.POST, request.FILES, instance=pred)
        pred = form.save()
        ist = IstorijaIzmenaPredmeta()
        ist.predmet = pred
        ist.radnik = request.user.radnik
        ist.timestamp = datetime.now()
        ist.save()
        return redirect('index')
    else:
        form = PredmetForm(instance=pred)
    context = {'form': form}
    return render(request, 'osnovni/predmet.html', context)


