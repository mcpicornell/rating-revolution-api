from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rating_revolution.models.reviewer import Reviewer
from rating_revolution.serializers.reviewer import ReviewerSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ReviewerViewSet(viewsets.ModelViewSet):
    queryset = Reviewer.objects.filter(is_active=True)
    serializer_class = ReviewerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'is_active']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Reviewer.objects.all()
        return Reviewer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)