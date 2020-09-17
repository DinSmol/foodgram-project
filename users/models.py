from django.db import models
from recipes.models import Recipe


class UserProfile(models.Model):
    favorites = models.ManyToManyField(Recipe, related_name='favorited_by')
