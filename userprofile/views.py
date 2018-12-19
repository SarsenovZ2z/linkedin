from django.shortcuts import render
from cities.models import City

# Create your views here.
def profileEdit(request):
    if request.method == 'POST':
        return print(request.POST)
    else:
        cities = City.objects.all()
        return render(request, 'profile/edit.html', {'cities': cities})
