from django.conf.urls import url
from osnovni.views import index

urlpatterns = [
    url(r'^$', index),
]