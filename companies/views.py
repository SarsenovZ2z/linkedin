from django.shortcuts import render
from cities.models import City
from .models import Company
# Create your views here.
def companyCreate(request):
    if request.method=='POST':
        return print(request.POST)
    else:
        cities = City.objects.all();
        types = Company.COMPANY_TYPES
        return render(request, "company/create.html", {'cities': cities, 'types': types})

def companyEdit(request):
    if request.method=='POST':
        return print(request.POST)
    else:
        cities = City.objects.all();
        types = Company.COMPANY_TYPES
        return render(request, "company/edit.html", {'cities': cities, 'types': types})
