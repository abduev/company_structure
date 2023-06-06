from django.db.models import Sum
from rest_framework import serializers

from employee.serializers import EmployeeSerializer
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)
    num_employees = serializers.SerializerMethodField()
    total_salary = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('name', 'employees', 'num_employees', 'total_salary')

    def get_num_employees(self, obj):
        return obj.employees.count()

    def get_total_salary(self, obj):
        return obj.employees.aggregate(
            total_salary=Sum('salary')).get('total_salary') or 0
