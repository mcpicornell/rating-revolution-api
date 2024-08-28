from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from rating_revolution.models.reviewer import Reviewer
from rating_revolution.serializers.reviewer import ReviewerSerializer
from rating_revolution.views.utils import CustomDestroyModelMixin


class ReviewerViewSet(CustomDestroyModelMixin, viewsets.ModelViewSet):
    queryset = Reviewer.objects.filter(is_active=True)
    serializer_class = ReviewerSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'is_active']

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Reviewer.objects.all()
        return Reviewer.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reviewer_validated_data = serializer.validated_data
        email = reviewer_validated_data.pop('email')
        password = make_password(reviewer_validated_data['password'])
        user = User.objects.create(
            username=email,
            email=email,
            password=password,
        )
        reviewer_validated_data.pop('password')
        reviewer_validated_data['user'] = user
        reviewer = Reviewer.objects.create(**reviewer_validated_data)
        response_serializer = self.get_serializer(reviewer)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
