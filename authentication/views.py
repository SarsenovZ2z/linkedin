from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import User

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
            return print(request.user)
        except:
            print("ERROR")
    else:
        return render(request, 'registration/registration.html')
