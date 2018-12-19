from django.shortcuts import render
from .models import User_CV
# Create your views here.
def cvCreate(request):
    if request.method == 'POST':
        return print(request.POST)
    else:
        return render(request, 'cv/create.html')


def cvEdit(request):
    if request.method == 'POST':
        return print(request.POST)
    else:
        return render(request, 'cv/edit.html')

def vacancyCreate(request):
    if request.method == 'POST':
        return print(request.POST)
    else:
        return render(request, 'vacancy/create.html')

def vacancyEdit(request):
    if request.method == 'POST':
        return print(request.POST)
    else:
        return render(request, 'vacancy/edit.html')

def userVacancyResponse(request):
    if request.method == 'POST':
        return print(request.POST)
    else:
        cvs = User_CV.objects.filter(user=request.user.id)
        return render(request, 'response/user.html', {'cvs': cvs})

def companyVacancyResponse(request):
    if request.method == 'POST':
        return print(request.POST)
    else:
        cvs = User_CV.objects.filter(user=request.user.id)
        return render(request, 'response/company.html', {'cvs': cvs})
