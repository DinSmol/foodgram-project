from django.db import models
from recipes.models import Recipe

# Create your models here.
class UserProfile(models.Model):
    favorites = models.ManyToManyField(Recipe, related_name='favorited_by')
