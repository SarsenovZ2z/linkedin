from django.urls import path,include
from .views import *

urlpatterns = [
    path('cv/create/', cvCreate, name='resume-create'),
    path('cv/edit/', cvEdit, name='resume-edit'),
    path('vacancy/create/', vacancyCreate, name='vacancy-create'),
    path('vacancy/edit/', vacancyEdit, name='vacancy-edit'),
    path('vacancy/response/user/', userVacancyResponse, name='uers-vacancy-response'),
    path('vacancy/response/company/', companyVacancyResponse, name='company-vacancy-response'),
]
