from django.db import models
from ingredients.models import Ingredient
from django.contrib.auth.models import User


class Tag(models.Model):
    tag_name = models.CharField('Name',max_length = 20, null=True)
    value = models.CharField('Value', max_length=64)
    style = models.CharField('Style', max_length=64, null=True)

    def __str__(self):
        return self.tag_name
        

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.ingredient.name


class Recipe(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(User, related_name="recipe_user", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', blank=True)   #  add default picture
    description = models.TextField()
    ingredients = models.ManyToManyField(RecipeIngredient)
    tag = models.ManyToManyField(Tag)
    cooking_duration = models.IntegerField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    favourite = models.ManyToManyField(User, related_name="fav_recipes", blank=True)

    def __str__(self):
        return self.title

    @property
    def taglist(self):
        return list(self.tag.all())

    @property
    def ingredientlist(self):
        return list(self.ingredients.all())


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")


