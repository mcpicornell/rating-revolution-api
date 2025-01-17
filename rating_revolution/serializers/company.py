from rest_framework import serializers
from rating_revolution.models import Company, Review, CompanyPhotos


class CompanySerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)
    photos = serializers.SerializerMethodField(read_only=True)
    rating = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(write_only=True, required=False)
    last_reviewer = serializers.SerializerMethodField(read_only=True)
    total_reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        exclude = ('is_active', 'user', )

    def get_reviews(self, obj):
        from .review import ReviewSerializer
        reviews = Review.objects.filter(company=obj, is_active=True)

        if self.context:
            view = self.context.get('view')
            if view and view.action == 'retrieve':
                return ReviewSerializer(reviews, many=True).data
        return reviews.count()

    @staticmethod
    def get_total_reviews(obj):
        return Review.objects.filter(company=obj, is_active=True).count()

    @staticmethod
    def get_last_reviewer(obj):
        from .reviewer import ReviewerSerializer
        reviews = Review.objects.filter(company=obj, is_active=True).order_by('-date')
        if reviews:
            last_reviewer= reviews.first().reviewer
            serializer = ReviewerSerializer(last_reviewer)
            return serializer.data
        return None


    @staticmethod
    def get_rating(obj):
        return str(obj.get_rating())

    def get_photos(self, obj):
        photos = CompanyPhotos.objects.filter(company=obj, is_active=True)
        if self.context and self.context['view'].action == 'retrieve':
            return [photo.url for photo in photos]
        first_photo = photos.first()
        return first_photo.url if first_photo else None

class CompanyPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyPhotos
        exclude = ('company', 'is_active')

