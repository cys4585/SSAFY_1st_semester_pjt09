from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    like_genre = models.CharField(max_length=50, blank=True)
