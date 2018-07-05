from django.urls import re_path
from .views import index

'''
matches anything except api
'''
urlpatterns = [
    re_path(r'^(?!api).*$', index, name='index'),
]