import statistics

from django.db import models
from rest_framework.authtoken.admin import User


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CIF = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def get_rating(self):
        from rating_revolution.models import Review
        reviews_values = Review.objects.filter(company=self).values_list('rating', flat=True)
        rating = statistics.mean(reviews_values) if len(reviews_values) > 0 else 0
        return round(rating, 1)


class CompanyPhotos(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    url = models.URLField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
