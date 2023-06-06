from rest_framework import mixins, permissions, viewsets
from rest_framework.viewsets import GenericViewSet

from .models import Department
from .serializers import DepartmentSerializer


class DepartmentViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny, )
    serializer_class = DepartmentSerializer
    search_fields = ('last_name',)
    queryset = Department.objects.all()
