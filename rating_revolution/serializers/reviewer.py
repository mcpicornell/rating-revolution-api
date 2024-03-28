from rest_framework import serializers
from rating_revolution.models.reviewer import Reviewer


class ReviewerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Reviewer
        fields = '__all__'
        read_only_fields = ('id', 'date', 'is_active')
