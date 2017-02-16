#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import simplejson
from PIL import Image

from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django_tables2 import RequestConfig
from orgsema import emails
from orgsema.forms import ForgotPasswordForm, PromenaLozinkeForm, MojiPodaciForm, NoviRadnikForm
from orgsema.models import Radnik
from orgsema.tables import ListaRadnika


def generate_password():
    """
    Generise novu lozinku od velikih latinicnih slova i cifara duzine 12 znakova.
    """
    digits = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V",
              "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    random.shuffle(digits)
    return "".join(digits[:12])


def forgotpass(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        # ako ne postoji dati email u bazi, forma nece biti validna pa ce se samo
        # uraditi redirekcija na / odnosno ponovo na login stranicu
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.get(email__iexact=email)
            new_password = generate_password()
            user.set_password(new_password)
            user.save()
            emails.send_password_mail(user.username, new_password, email)
        return redirect('/')


@login_required
def changepassword(request):
    if request.method == 'POST':
        form = PromenaLozinkeForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])
            if user.check_password(form.cleaned_data['old_password']):
                user.set_password(form.cleaned_data['new_password1'])
                user.save()
                update_session_auth_hash(request, user)
                return redirect('changepass2')
    else:
        form = PromenaLozinkeForm(initial={'username': request.user.username})
    return render(request, 'orgsema/changepassword.html', {'form': form, 'breadcrumbs': [u'Promena lozinke']})


@login_required
def changepassword2(request):
    return render(request, 'orgsema/changepassword2.html', {'breadcrumbs': [u'Promena lozinke']})


@login_required
def myprofile(request):
    if request.method == 'POST':
        form = MojiPodaciForm(request.POST)
        if form.is_valid():
            request.user.first_name = form.cleaned_data['ime']
            request.user.last_name = form.cleaned_data['prezime']
            request.user.email = form.cleaned_data['email']
            request.user.radnik.orgjed = form.cleaned_data['org_jed']
            request.user.save()
            return redirect('myprofile')
    else:
        current = {
            'username': request.user.username,
            'ime': request.user.first_name,
            'prezime': request.user.last_name,
            'email': request.user.email,
            'org_jed': request.user.radnik.orgjed.pk
        }
        form = MojiPodaciForm(initial=current)
    return render(request, 'orgsema/myprofile.html', {'form': form, 'breadcrumbs': [u'Moj profil']})


@login_required
def newemployee(request):
    if request.method == 'POST':
        form = NoviRadnikForm(request.POST)
        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data['ime']
            user.last_name = form.cleaned_data['prezime']
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.is_staff = (form.cleaned_data['uloga'].id == 1)
            user.is_superuser = (form.cleaned_data['uloga'].id == 1)
            user.save()
            radnik = Radnik()
            radnik.user = user
            radnik.orgjed = form.cleaned_data['org_jed']
            radnik.uloga = form.cleaned_data['uloga']
            radnik.save()
            return redirect('newemployee2', radnik.id)
    else:
        form = NoviRadnikForm()
    return render(request, 'orgsema/newemployee.html', {'form': form, 'breadcrumbs': [u'Novi korisnik']})


@login_required
def newemployee2(request, radnik_id):
    try:
        radnik = Radnik.objects.get(id=radnik_id)
        return render(request, 'orgsema/newemployee2.html', {'radnik': radnik})
    except Exception as err:
        print(err)
        return redirect('/')


@login_required
def employeelist(request):
    table = ListaRadnika(Radnik.objects.all())
    RequestConfig(request, paginate={"per_page": 20}).configure(table)
    return render(request, 'orgsema/employeelist.html', {'breadcrumbs': [u'Korisnici'], 'table': table})


@login_required
def upload_avatar(request):
    radnik = request.user.radnik
    for fajl in request.FILES.getlist('avatar'):
        radnik.avatar.save(fajl.name, ContentFile(fajl.read()))
    radnik.save()
    oldimage = Image.open(radnik.avatar.file.name)
    width, height = oldimage.size
    minimum = min(width, height)
    cropwidth = (width-minimum)//2
    cropheight = (height-minimum)//2
    newimage = oldimage.crop((cropwidth, cropheight, width-cropwidth, height-cropheight))
    newimage.save(radnik.avatar.file.name)
    return HttpResponse(simplejson.dumps({'url': radnik.avatar.url}),  mimetype="application/x-javascript")
