from django.shortcuts import render
from cities.models import City
from .models import Company
# Create your views here.
def companyCreate(request):
    if request.method=='POST':
        company = Company()
        company.user = request.user
        company.city = City.objects.get(pk=request.POST['city'])
        company.description = request.POST['description']
        company.name = request.POST['name']
        company.short_description = request.POST['short_description']
        company.site = request.POST['site']
        company.short_name = request.POST['short_name']
        company.COMPANY_TYPES = request.POST['type']
        company.save()
    else:
        cities = City.objects.all();
        types = Company.COMPANY_TYPES
        return render(request, "company/create.html", {'cities': cities, 'types': types})

def companyEdit(request):
    if request.method=='POST':
        company = Company.objects.get(user=request.user.id)
        company.user = request.user
        company.city = City.objects.get(pk=request.POST['city'])
        company.description = request.POST['description']
        company.name = request.POST['name']
        company.short_description = request.POST['short_description']
        company.site = request.POST['site']
        company.short_name = request.POST['short_name']
        company.COMPANY_TYPES = request.POST['type']
        company.save()

    else:
        cities = City.objects.all();
        types = Company.COMPANY_TYPES
        return render(request, "company/edit.html", {'cities': cities, 'types': types})

def companies(request):
    companies = Company.objects.all()
    return render(request, 'company/show.html', {'companies': companies})
