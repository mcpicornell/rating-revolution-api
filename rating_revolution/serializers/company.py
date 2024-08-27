from rest_framework import serializers
from rating_revolution.models import Company, Review, CompanyPhotos


class CompanySerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)
    photos = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Company
        exclude = ('is_active', 'user', )

    def get_reviews(self, obj):
        reviews = Review.objects.filter(company=obj, is_active=True)
        if self.context['view'].action == 'retrieve':
            return reviews
        return reviews.count()

    @staticmethod
    def get_photos(obj):
        return CompanyPhotos.objects.filter(company=obj, is_active=True)

class CompanyPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyPhotos
        exclude = ('company', 'is_active')

