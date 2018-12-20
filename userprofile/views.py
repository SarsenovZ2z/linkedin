from django.shortcuts import render
from cities.models import City
from .models import Profile
# Create your views here.
def profileEdit(request):
    if request.method == 'POST':
        p = Profile.objects.get(user=request.user.id)
        p.user = request.user
        p.city = City.objects.get(pk=request.POST['city'])
        p.phone = request.POST['phone']
        p.skype = request.POST['skype']
        p.date_of_birth = request.POST['date_of_birth']
        p.image = request.POST['image']
        p.save()
    else:
        cities = City.objects.all()
        return render(request, 'profile/edit.html', {'cities': cities})

def profile(request):
    user = request.user
    return render(request, 'profile/show.html', {'user': user})
