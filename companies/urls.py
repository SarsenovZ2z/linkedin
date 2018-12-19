from django.urls import path,include
from .views import *

urlpatterns = [
    path('create/', companyCreate, name='company-create'),
    path('edit/', companyEdit, name='company-edit'),
]
