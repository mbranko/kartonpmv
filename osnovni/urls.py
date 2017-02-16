from django.conf.urls import url
from osnovni.views import index, novi_predmet, predmet, pretraga

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^novi/$', novi_predmet, name='novi'),
    url(r'^karton/(?P<predmet_id>\d+)/$', predmet, name='edit'),
    url(r'^pretraga/$', pretraga, name='pretraga'),
]