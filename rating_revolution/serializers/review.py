from rest_framework import serializers

from rating_revolution.models import Review
from .reviewer import ReviewerSerializer
from .company import CompanySerializer


class ReviewSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()
    company = CompanySerializer(read_only=True)
    reviewer = ReviewerSerializer(read_only=True)

    class Meta:
        model = Review
        exclude = ('is_active',)

    @staticmethod
    def get_likes(obj):
        return obj.get_likes()

    @staticmethod
    def get_dislikes(obj):
        return obj.get_dislikes()


class ReviewEventSerializer(serializers.Serializer):
    pass
