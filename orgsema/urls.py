from django.urls import path
from orgsema.views import *

urlpatterns = [
    path('forgotpass/', forgotpass, name='forgotpass'),
    path('changepass/', changepassword, name='changepass'),
    path('changepass2/', changepassword2, name='changepass2'),
    path('profile/', myprofile, name='myprofile'),
    path('newuser/', newemployee, name='newemployee'),
    path('newuser/<int:radnik_id>/', newemployee2, name='newemployee2'),
    path('users/', employeelist, name='employeelist'),
    path('user/upload/avatar/', upload_avatar, name='upload_avatar'),
]