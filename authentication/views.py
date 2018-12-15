from django.shortcuts import render

# Create your views here.
def testuser(request):
    print(request.user)
