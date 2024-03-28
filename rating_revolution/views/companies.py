from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rating_revolution.models.company import Company
from rating_revolution.serializers import CompanySerializer
from rating_revolution.views.utils import CustomDestroyModelMixin


class CompanyViewSet(CustomDestroyModelMixin, viewsets.ModelViewSet):
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_active']

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated]
        return super().get_permissions()
