from django.contrib import admin
from .models import *


class CityInline(admin.TabularInline):
    model = City;
    extra = 0

class InstitutionInline(admin.TabularInline):
    model = Institution;
    extra = 0

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    inlines = [
        CityInline
    ]


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    inlines = [
        InstitutionInline
    ]

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'short_name')

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Institution, InstitutionAdmin)
