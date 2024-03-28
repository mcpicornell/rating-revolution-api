from django.db import models
from rating_revolution import settings


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    CIF = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class CompanyPhotos(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    photo = models.URLField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
