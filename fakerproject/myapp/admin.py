from django.contrib import admin
from myapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    l = ['names','roll','marks','dob','email']
admin.site.register(Student,StudentAdmin)
