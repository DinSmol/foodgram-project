import csv
from ingredients.models import Ingredient


def data_upl(request):
    with open('ingredients.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Ingredient.objects.get_or_create(
                name=row[0],
                units=row[1],
                )


from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import IngredientSerializer
import csv
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import JsonResponse


class Ingredients(View):
    def get(self, request):
        text = request.GET['query']
        ings = Ingredient.objects.filter(name__contains=text).values('name', 'units'). order_by()
        print(ings)
        return JsonResponse(list(ings), safe=False)

def get_ingredients(request):
    ingredients = {}
    for key in request.POST:
        if key.startswith('nameIngredient'):
            val_key = key.replace('name', 'value')
            ingredients[request.POST[key]] = request.POST[val_key]
    return ingredients
    