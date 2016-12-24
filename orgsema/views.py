#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from orgsema import emails
from orgsema.forms import ForgotPasswordForm, PromenaLozinkeForm


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
            if request.user.check_password(form.cleaned_data['old_password']):
                request.user.set_password(form.cleaned_data['new_password1'])
                request.user.save()
                return redirect('orgsema.views.changepassword2')
    else:
        form = PromenaLozinkeForm(initial={'username': request.user.username})
    return render_to_response('orgsema/changepassword.html',
                              {'form': form,
                               'breadcrumbs': [u'Promena lozinke'],
                               'maintitle': u'Promena lozinke',
                               'titleinfo': u'Morate znati tekuću lozinku da biste je promenili',
                              })


@login_required
def changepassword2(request):
    return render_to_response('orgsema/changepassword2.html',
        {'breadcrumb1': u'Лозинка',
         'naslov': u'Промена лозинке',
        },
        context_instance=RequestContext(request))


