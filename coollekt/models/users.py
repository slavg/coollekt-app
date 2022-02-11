from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length=500, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
