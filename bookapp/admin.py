from django.contrib import admin
from .models import Book,Employee
# Register your models here.
admin.site.register(Book)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']


admin.site.register(Employee, EmployeeAdmin)