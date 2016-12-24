from django import forms
from django.contrib.auth.models import User


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

