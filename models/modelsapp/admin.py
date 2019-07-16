from django.contrib import admin
from .models import student

class student(admin.ModelAdmin): 

     admin.site.register(student)