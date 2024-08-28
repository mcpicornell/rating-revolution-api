from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from rating_revolution.models.company import Company
from rating_revolution.serializers import CompanySerializer
from rating_revolution.serializers.company import CompanyPhotoSerializer
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company_validated_data = serializer.validated_data
        email = company_validated_data['email']
        password = make_password(company_validated_data['password'])
        user = User.objects.create(
            username=email,
            email=email,
            password=password,
        )
        company_validated_data.pop('password')
        company_validated_data['user'] = user
        company = Company.objects.create(**company_validated_data)
        response_serializer = self.get_serializer(company)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], url_path="photo", serializer_class=CompanyPhotoSerializer)
    def add_photo(self, request, pk=None):
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanyPhotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(company=company)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
