from django.contrib import admin
from .models import *

class User_profileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city')


admin.site.register(User_profile, User_profileAdmin)