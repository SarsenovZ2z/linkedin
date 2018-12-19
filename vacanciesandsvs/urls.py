from django.urls import path,include
from .views import *

urlpatterns = [
    path('create/', cvCreate, name='resume-create'),
    path('edit/', cvEdit, name='resume-edit'),
]
