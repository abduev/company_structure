from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions, viewsets

from .filters import EmployeeFilter
from .models import Employee
from .pagination import EmployeePagination
from .serializers import EmployeeSerializer


class EmployeeViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EmployeeFilter
    pagination_class = EmployeePagination
    queryset = Employee.objects.all()
