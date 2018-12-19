from django.shortcuts import render

# Create your views here.
def cvCreate(request):
    if request.method == 'POST':
        return print(request.POST)
    else:
        return render(request, 'cv/create.html')


def cvEdit(request):
    if request.method == 'POST':
        return print(request.POST)
    else:
        return render(request, 'cv/edit.html')
