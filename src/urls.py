from django.urls import re_path, path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('XXXXXXXXXXX.urls')),
]
