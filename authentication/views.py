from django.shortcuts import render
from django.conf import settings
# Create your views here.

def register(request):
    if request.method == "POST":
        print(request.POST)
    else:
        return render(request, 'registration/registration.html')
