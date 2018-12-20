from django.shortcuts import render
from .models import *

def cvCreate(request):
    if request.method == 'POST':
        cv = User_CV()
        cv.user = request.user
        cv.name = request.POST['name']
        cv.description_short = request.POST['description_short']
        cv.description = request.POST['description']
        cv.content = request.POST['content']
        cv.save()
    else:
        return render(request, 'cv/create.html')


def cvEdit(request):
    if request.method == 'POST':
        u = User()
        cv = User_CV.objects.get(pk=request.POST['cv_id'])
        cv.user = request.user
        cv.name = request.POST['name']
        cv.content = request.POST['content']
        cv.description = request.POST['description']
        cv.description_short = request.POST['description_short']
        cv.save()
        return print('duris')
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

def vacancies(request):
    vacncies = Vacancy.objects.all()
    return render(request, 'vacancy/show.html', {'vacancies': vacancies})

def cvs(request):
    cvs = Vacancy.objects.all()
    return render(request, 'cv/show.html', {'cvs': cvs})
