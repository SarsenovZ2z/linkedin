from django.contrib import admin
from .models import *


class EducationAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'code')

admin.site.register(Education, EducationAdmin)


class CvAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'code')

admin.site.register(User_CV, CvAdmin)
admin.site.register(Vacancy)
