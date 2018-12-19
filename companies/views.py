from django.shortcuts import render
from .models import Company
# Create your views here.
def companyCreate(request):
    types = Company.COMPANY_TYPES
    return render(request, "company/create.html", {'types': types})

def companyEdit(request):
    types = Company.COMPANY_TYPES
    return render(request, "company/edit.html", {'types': types})
