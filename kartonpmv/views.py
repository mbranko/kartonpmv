import random
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import redirect
from kartonpmv.forms import ForgotPasswordForm
from kartonpmv import emails


def logout(request):
    auth.logout(request)
    return redirect('/')


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
            emails.send_password_mail(new_password, email)
        return redirect('/')
