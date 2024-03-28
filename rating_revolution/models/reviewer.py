from django.db import models
from rating_revolution.settings import AVATAR_DEFAULT_URL
from django.conf import settings


class Reviewer(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, unique=True)
    avatar = models.URLField(max_length=255, default=AVATAR_DEFAULT_URL)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

