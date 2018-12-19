from django.contrib import admin
from .models import *


class EducationAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'code')
    
admin.site.register(Education, EducationAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city')

admin.site.register(Profile, ProfileAdmin)
