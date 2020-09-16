import csv

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from ingredients.models import Ingredient
from recipes.models import RecipeIngredient
from rest_framework import status, viewsets
from rest_framework.permissions import (IsAuthenticated,
										IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from .serializers import IngredientSerializer


def data_upl(request):
	with open('ingredients.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			_, created = Ingredient.objects.get_or_create(
				name=row[0],
				units=row[1],
				)




class Ingredients(View):
	def get(self, request):
		text = request.GET['query']
		ings = Ingredient.objects.filter(name__contains=text).values('name', 'units'). order_by()
		print(ings)
		return JsonResponse(list(ings), safe=False)

def get_ingredients(request):
	res = []
	for key in request.POST:
		if key.startswith('nameIngredient'):
			val_key = key.replace('name', 'value')
			ing_id = key.replace('nameIngredient_', '')
			print(request.POST[key])
			ingredient = Ingredient.objects.get(name=request.POST[key])
			rec_ingredient = RecipeIngredient.objects.get_or_create(ingredient=ingredient, quantity=request.POST[val_key])
			res.append(rec_ingredient[0])
	print(res)
	return res
