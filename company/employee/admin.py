from django.contrib import admin

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ['last_name', 'department']
    list_display = ('first_name', 'last_name', 'department',)
    model = Employee


admin.site.register(Employee, EmployeeAdmin)
