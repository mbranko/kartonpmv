#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.mail import EmailMultiAlternatives

FORGOT_PASSWORD_TITLE = "Osnovni karton muzejskog predmeta: Nova lozinka"
FORGOT_PASSWORD_TEXT = u"""

Dragi korisniče,

Neko je zatražio generisanje nove Vaše lozinke.

Vaša stara lozinka je obrisana, a nova lozinka glasi:
%s

Molimo Vas da se što pre prijavite i promenite lozinku.

Sa poštovanjem,
Osnovni karton muzejskog predmeta
Pozorišni muzej Vojvodine

"""
FORGOT_PASSWORD_HTML = u"""

<p>Dragi korisniče,</p>

<p>Neko je zatražio generisanje nove Vaše lozinke.</p>

<p>Vaša stara lozinka je obrisana, a nova lozinka glasi:<br/>
<pre>
%s
</pre>
</p>

<p>Molimo Vas da se što pre prijavite i promenite lozinku.</p>

<p>Sa poštovanjem,<br/>
Osnovni karton muzejskog predmeta<br/>
Pozorišni muzej Vojvodine</p>

"""


def send_password_mail(password, recipient):
    msg = EmailMultiAlternatives(
        subject=FORGOT_PASSWORD_TITLE,
        body=FORGOT_PASSWORD_TEXT % password,
        to=[recipient])
    msg.attach_alternative(FORGOT_PASSWORD_HTML % password, 'text/html')
    msg.send()
