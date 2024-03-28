
from rest_framework import viewsets, permissions
from rating_revolution.models import Review
from rating_revolution.serializers import ReviewSerializer
from rating_revolution.views.utils import CustomDestroyModelMixin


class ReviewViewSet(CustomDestroyModelMixin, viewsets.ModelViewSet):
    queryset = Review.objects.filter(is_active=True)
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




