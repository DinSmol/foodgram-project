from django.db import models
from ingredients.models import Ingredient
from django.contrib.auth.models import User


class Tag(models.Model):
    TAG_CHOICES = (
        ('Завтрак', 'Завтрак'),
        ('Обед', 'Обед'),
        ('Ужин', 'Ужин'),
    )
    tag_name = models.CharField(max_length = 20, choices=TAG_CHOICES)

    def __str__(self):
        return self.tag_name
        

class Recipe(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    tag = models.ManyToManyField(Tag)
    cooking_duration = models.IntegerField()
    slug = models.SlugField()

    def __str__(self):
        return self.name


