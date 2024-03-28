
from rest_framework import serializers
from rating_revolution.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'company': {'write_only': True},
            'reviewer': {'write_only': True},
        }
