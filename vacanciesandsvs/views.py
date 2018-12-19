from django.shortcuts import render

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
        cvs = request.user.cv_set.all()
        return render(request, 'response/user.html', {'cvs': cvs})

def companyVacancyResponse(request):
    if request.method == 'POST':
        return print(request.POST)
    else:
        cvs = request.user.cv_set.all()
        return render(request, 'response/company.html', {'cvs': cvs})
