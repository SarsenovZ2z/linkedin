from django.contrib import admin
from .models import *

# Register your models here.
class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    list_display = ('name', 'city', 'short_description', 'company_type')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'short_description', 'company_type')
    inlines = [
        PostInline
    ]

admin.site.register(Company, CompanyAdmin)
