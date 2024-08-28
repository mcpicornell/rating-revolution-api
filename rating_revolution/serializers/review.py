from rest_framework import serializers

from rating_revolution.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()

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
