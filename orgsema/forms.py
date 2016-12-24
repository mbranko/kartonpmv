#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import forms
from django.contrib.auth.models import User
from models import OrgJed, Uloga


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label=u'email', max_length=100)

    def clean(self):
        em = self.cleaned_data.get('email')
        if em is not None:
            try:
                User.objects.get(email=em)
            except:
                raise forms.ValidationError("Nema korisnika sa datim emailom.")
        return self.cleaned_data


class NoviRadnikForm(forms.Form):
    ime = forms.CharField(label=u'ime', max_length=30)
    prezime = forms.CharField(label=u'prezime', max_length=30)
    org_jed = forms.ModelChoiceField(label=u'organizaciona jedinica', queryset=OrgJed.objects.filter(aktivna=True))
    uloga = forms.ModelChoiceField(label=u'uloga', queryset=Uloga.objects.all(), initial=3)
    username = forms.CharField(label=u'korisničko ime', max_length=30)
    password1 = forms.CharField(label=u'lozinka', max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'ponovljena lozinka', max_length=30, widget=forms.PasswordInput)
    email = forms.EmailField(label=u'email', max_length=100)

    def clean(self):
        test_username = self.cleaned_data['username']
        u = User.objects.filter(username__iexact=test_username)
        if u.exists():
            raise forms.ValidationError(u"Korisničko ime je već zauzeto.")
        pw1 = self.cleaned_data.get('password1')
        pw2 = self.cleaned_data.get('password2')
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            del self.cleaned_data['password1']
            del self.cleaned_data['password2']
            raise forms.ValidationError("Unete lozinke nisu jednake.")
        return self.cleaned_data


class PromenaLozinkeForm(forms.Form):
    username = forms.CharField(label=u'korisničko ime', max_length=30, widget=forms.HiddenInput)
    old_password = forms.CharField(label=u'sadašnja lozinka', max_length=30, widget=forms.PasswordInput)
    new_password1 = forms.CharField(label=u'nova lozinka', max_length=30, widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=u'nova lozinka', max_length=30, widget=forms.PasswordInput)

    def clean(self):
        un = self.cleaned_data.get('username')
        ow = self.cleaned_data.get('old_password')
        pw1 = self.cleaned_data.get('new_password1')
        pw2 = self.cleaned_data.get('new_password2')
        if ow is not None:
            user = User.objects.get(username__exact=un)
            if not user.check_password(ow):
                raise forms.ValidationError("Trenutna lozinka je pogrešna.")
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            del self.cleaned_data['new_password1']
            del self.cleaned_data['new_password2']
            raise forms.ValidationError("Unete lozinke nisu jednake.")
        return self.cleaned_data


class MojiPodaciForm(forms.Form):
    username = forms.CharField(label=u'korisničko ime', max_length=30, widget=forms.HiddenInput)
    ime = forms.CharField(label=u'ime', max_length=30)
    prezime = forms.CharField(label=u'prezime', max_length=30)
    email = forms.EmailField(label='email', max_length=100)
    org_jed = forms.ModelChoiceField(label=u'organizaciona jedinica', queryset=OrgJed.objects.filter(aktivna=True))
