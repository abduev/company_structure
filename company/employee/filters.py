from django_filters import CharFilter, FilterSet, NumberFilter

from .models import Employee


class EmployeeFilter(FilterSet):
    last_name = CharFilter(field_name='last_name', lookup_expr='istartswith')
    department_id = NumberFilter(field_name='department')

    class Meta:
        model = Employee
        fields = ('last_name', 'department_id')
