"""kartonpmv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from kartonpmv import settings, views

urlpatterns = [
    path('accounts/login/', LoginView.as_view()),
    path('accounts/logout/', views.logout, name='logout'),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('orgsema/', include('orgsema.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('osnovni.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
