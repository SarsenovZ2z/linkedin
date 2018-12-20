from django.urls import path,include
from .views import *

urlpatterns = [
    path('edit/', profileEdit, name='profile-edit'),
    path('', profile, name='profile'),
]
