from django.db import models
from authentication.models import User
from cities.models import City
from institutions.models import Institution
from companies.models import Company
import datetime



def year_choices():
    return [(r,r) for r in range(1900, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE,null=True)
    year_receipt = models.IntegerField('ASD', choices=year_choices(), default=current_year)
    year_graduation = models.IntegerField('ASD2', choices=year_choices(), default=current_year)
    degree = models.CharField(max_length=255)


class Vacancy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    description_short = models.TextField()
    salary = models.IntegerField()
    content = models.TextField()
    date_created = models.DateField(auto_now_add=True)


class User_CV(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    description_short = models.TextField()
    content = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True)

class Vacancy_response(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    cv = models.ForeignKey(User_CV, on_delete=models.CASCADE,null=True)
    message = models.TextField(null=True)# Userdin jibergen message
    seen = models.BooleanField(default=False)
    respose = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True)
    date_responded = models.DateField(auto_now=True)

class User_experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True)
    date_start = models.DateField()
    date_end = models.DateField()
