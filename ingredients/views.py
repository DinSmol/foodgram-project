import csv

from django.http import JsonResponse
from django.views.generic import View
from ingredients.models import Ingredient
from recipes.models import RecipeIngredient


class Ingredients(View):
    def get(self, request):
        text = request.GET['query']
        ings = Ingredient.objects.filter(
            name__istartswith =text).values('name', 'units').order_by('name')
        return JsonResponse(list(ings), safe=False)


def get_ingredients(request):
    res = []
    for key in request.POST:
        if key.startswith('nameIngredient'):
            val_key = key.replace('name', 'value')
            ingredient = Ingredient.objects.get(name=request.POST[key])
            rec_ingredient = RecipeIngredient.objects.get_or_create(
                ingredient=ingredient,
                quantity=request.POST[val_key])
            res.append(rec_ingredient[0])
    return res
