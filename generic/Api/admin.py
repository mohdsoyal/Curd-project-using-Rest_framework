from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

# Register your models here.

class modaladmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
admin.site.register(Student,modaladmin)
