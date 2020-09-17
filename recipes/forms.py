from django.forms import ModelForm
from recipes.models import Ingredient, Recipe


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name", "units")


class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = ("title", "tag", 'cooking_duration', 'description', 'image')
