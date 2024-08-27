from django.db import models
from rating_revolution.settings import AVATAR_DEFAULT_URL
from rest_framework.authtoken.admin import User


class Reviewer(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, unique=True)
    avatar = models.URLField(max_length=255, default=AVATAR_DEFAULT_URL)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

