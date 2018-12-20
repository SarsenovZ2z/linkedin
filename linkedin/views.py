from django.shortcuts import render
from vacanciesandsvs.models import Vacancy, User_CV

def index(request):
    number_of_vacancies = Vacancy.objects.count()
    number_of_cv = User_CV.objects.count()
    user_id = request.user.id
    user_cv = User_CV.objects.filter(user=user_id)
    ress = Vacancy_response.objects.all()
    return render(request, 'pages/index.html', {'user': request.user,
                                                'number_of_vacancies':number_of_vacancies,
                                                'number_of_cvs':number_of_cv,
                                                'cvs':user_cv,
                                                'ress': ress
                                                })
