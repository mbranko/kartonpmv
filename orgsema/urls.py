from django.conf.urls import url
from orgsema.views import forgotpass, changepassword, changepassword2

urlpatterns = [
    url(r'^forgotpass/$', forgotpass, name='forgotpass'),
    url(r'^changepass/$', changepassword, name='changepass'),
    url(r'^changepass2/$', changepassword2, name='changepass2'),
]