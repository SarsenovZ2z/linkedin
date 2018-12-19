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
