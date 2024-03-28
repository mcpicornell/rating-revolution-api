from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rating_revolution.models.company import Company
from rating_revolution.serializers import CompanySerializer
from rating_revolution.views.utils import CustomDestroyModelMixin


class CompanyViewSet(CustomDestroyModelMixin, viewsets.ModelViewSet):
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_active']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
