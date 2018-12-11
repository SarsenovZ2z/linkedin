from django.contrib import admin
from .models import *

# Register your models here.
class CityInline(admin.TabularInline):
    model = City;
    extra = 0

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    inlines = [
        CityInline
    ]


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
