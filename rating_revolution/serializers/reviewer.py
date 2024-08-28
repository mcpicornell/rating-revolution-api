from rest_framework import serializers

from rating_revolution.models import Reviewer, Review


class ReviewerSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True, required=True)
    reviews = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(write_only=True, required=True)
    rating =serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Reviewer
        exclude = ('user', 'is_active')
        read_only_fields = ('id', 'date', 'is_active')

    def get_reviews(self, obj):
        reviews = Review.objects.filter(reviewer=obj, is_active=True)
        if self.context and self.context['view'].action == 'retrieve':
            return reviews
        return reviews.count()

    @staticmethod
    def get_rating(obj):
        return obj.get_rating()
