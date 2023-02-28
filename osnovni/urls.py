from django.urls import path
from osnovni.views import index, novi_predmet, predmet, pretraga, moji_predmeti, statistika_unosa, inventarna_knjiga

urlpatterns = [
    path('novi/', novi_predmet, name='novi'),
    path('karton/<int:predmet_id>/', predmet, name='edit'),
    path('pretraga/', pretraga, name='pretraga'),
    path('moji/', moji_predmeti, name='moji'),
    path('statistika-unosa/', statistika_unosa, name='statistika_unosa'),
    path('inventarna-knjiga/', inventarna_knjiga, name='inventarna_knjiga'),
    path('inventarna-knjiga/<int:od>/<int:do>/', inventarna_knjiga, name='inventarna_knjiga_od_do'),
    path('', index, name='index'),
]
