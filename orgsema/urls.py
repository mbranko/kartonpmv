from django.conf.urls import url
from orgsema.views import *

urlpatterns = [
    url(r'^forgotpass/$', forgotpass, name='forgotpass'),
    url(r'^changepass/$', changepassword, name='changepass'),
    url(r'^changepass2/$', changepassword2, name='changepass2'),
    url(r'^profile/$', myprofile, name='myprofile'),
    url(r'^newuser/$', newemployee, name='newemployee'),
    url(r'^newuser/(?P<radnik_id>\d+)/$', newemployee2, name='newemployee2'),
    url(r'^users/$', employeelist, name='employeelist'),
    url(r'^user/upload/avatar/$', upload_avatar, name='upload_avatar'),
]