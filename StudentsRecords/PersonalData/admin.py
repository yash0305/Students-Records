from django.contrib import admin

from .models import StudentsData

class studentsData(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(StudentsData, studentsData)