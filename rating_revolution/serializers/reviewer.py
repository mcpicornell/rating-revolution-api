from rest_framework import serializers
from rating_revolution.models import Reviewer, Review


class ReviewerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Reviewer
        fields = '__all__'
        read_only_fields = ('id', 'date', 'is_active')

    def get_reviews(self, obj):
        reviews = Review.objects.filter(reviewer=obj, is_active=True)
        if self.context['view'].action == 'retrieve':
            return reviews
        return reviews.count()

