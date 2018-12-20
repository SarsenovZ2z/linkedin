from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import User
from companies.models import Company
from userprofile.models import Profile

def register(request):
    if request.method == "POST":
        try:
            user = User.objects.create_user(
                email=request.POST['email'],
                password=request.POST['password'],
            )
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            profile = Profile()
            profile.user = user
            profile.save()
            is_employer = (request.POST['is_employer']=='0')
            if (is_employer):
                company = Company()
                company.user = user
                company.save()

            return render(request, 'registration/edit.html', {'is_company': is_employer})
        except:
            return render(request, 'registration/edit.html', {'is_company': False})
    else:
        return render(request, 'registration/registration.html')

def edit(request):
    return render(request, "", {'is_company': request.GET['is_company']})
