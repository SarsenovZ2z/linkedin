from django.contrib import admin
from .models import *

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'short_name')

admin.site.register(Institution, InstitutionAdmin)
