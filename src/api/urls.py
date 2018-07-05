# Urls are simply redirect the request to the right view

from django.urls import re_path, path, include
from . import views


'''
##########################    Custom Email templates
'''
from djoser.email import *
from settings import BASE_DIR
import os
template_path = os.path.join(BASE_DIR, 'api/templates/email')
ActivationEmail.template_name = template_path+'/activation.html'
ConfirmationEmail.template_name = template_path+'/confirmation.html'
PasswordResetEmail.template_name = template_path+'/password_reset.html'


'''
##########################    User Auth and Profile:
http://djoser.readthedocs.io/en/latest/base_endpoints.html
'''
urlpatterns = [
    path('', include('djoser.urls.base')),
    path('', include('djoser.urls.authtoken')),
    path('', include('djoser.urls.jwt')),
    path('', include('djoser.social.urls')),
    re_path(r'^activate/(?P<uid>[A-Za-z0-9]+)/(?P<token>[A-Za-z0-9-]+)/$', views.ActivationLink.as_view()),  # links the user to the site and give activation credentials
    re_path(r'^password/reset/confirm/(?P<uid>[A-Za-z0-9]+)/(?P<token>[A-Za-z0-9-]+)/$', views.ResetConfirm.as_view()),

    path('showUsers/', views.UserList.as_view()),

    path('checkauth/', views.CheckAuth.as_view()),
    path('updateprofile/', views.UpdateProfile.as_view()),
]


'''
##########################    Generics
'''
urlpatterns += [
    path('rezept/all/', views.RezeptListView.as_view()),
    path('rezept/create/', views.RezeptCreateView.as_view()),
    re_path(r'rezept/rud/(?P<pk>\d+)/$', views.RezeptRudView.as_view()),
    # re_path(r'rud/title/(?P<titel>[\w-]+)/$', views.RezeptTitleRudView.as_view()),   # search by title
]


'''
##########################    API Custom Classes
'''
urlpatterns += [

]
