from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from rating_revolution.models import Review
from rating_revolution.models.review import ReviewEvent
from rating_revolution.serializers import ReviewSerializer, ReviewEventSerializer
from rating_revolution.views.utils import CustomDestroyModelMixin


class ReviewViewSet(CustomDestroyModelMixin, viewsets.ModelViewSet):
    queryset = Review.objects.filter(is_active=True)
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['reviewer', 'company']
    ordering_fields = ['date']
    ordering = ['-date']

    def get_serializer_class(self):
        if self.action in ['create_like_event', 'create_dislike_event']:
            return ReviewEventSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=['post'], url_path="like")
    def create_like_event(self, request, pk=None):
        ReviewEvent.objects.create(type=ReviewEvent.LIKE, review_id=pk)
        review = Review.objects.get(pk=pk)
        return Response({'detail': f'Like event created to review: {review.title}'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], url_path="dislike")
    def create_dislike_event(self, request, pk=None):
        ReviewEvent.objects.create(type=ReviewEvent.DISLIKE, review_id=pk)
        review = Review.objects.get(pk=pk)
        return Response(
            {'detail': f'Dislike event created to review: {review.title}'},
            status=status.HTTP_201_CREATED
        )
