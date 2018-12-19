from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('company/', include('companies.urls')),
    path('profile/', include('userprofile.urls')),
    path('cv/', include('vacanciesandsvs.urls')),
]
