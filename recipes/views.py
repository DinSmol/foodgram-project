from django.shortcuts import render
from recipes.forms import IngredientForm
from ingredients.models import Ingredient
from ingredients.views import get_ingredients
from recipes.models import Recipe, Follow
from django.views.decorators.http import require_POST
import json
from .forms import RecipeForm
from django.shortcuts import redirect
from recipes.models import Tag
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


def new(request):
	if request.method == 'POST':
		ingredients = get_ingredients(request)
		tags = get_tags(request)
		form = RecipeForm(request.POST, files=request.FILES or None)
		
		if form.is_valid():
			recipe = form.save(commit=False)
			recipe.author = request.user
			recipe.save()
			for tag in tags: recipe.tag.add(tag)
			for item in ingredients: recipe.ingredients.add(item)
			return redirect('index')
	else:
		form = RecipeForm()
		tags = {'Завтрак': 'Завтрак','Обед': 'Обед', 'Ужин': 'Ужин'}
	return render(request, 'formRecipe.html', {'form': form, 'tags': tags})

def recipe_delete(request, id):
	recipe = Recipe.objects.get(id=id)
	if recipe.author == request.user or request.user.is_superuser:
		recipe.delete()
	recipes = Recipe.objects.all().order_by('-created')
	return redirect('index')

def purchases(request):
	id = json.loads((request.body).decode('utf8'))['id']
	lst = Recipe.objects.get(id=id)
	print(lst.title)
	return render(request, 'shopList.html')


def get_tags(request):
	tags = []
	for key in request.POST.getlist('tag'):
		tags.append(Tag.objects.get(id=int(key)))
	return tags

def recipe_detail(request, id):
	recipe = Recipe.objects.get(id=id)
	# ingredients = get_ingredients(request)
	# tags = get_tags(request)
	form = RecipeForm(instance=recipe, files=request.FILES or None)
	tag_ids = []
	ingredients = []
	for tag_item in form.instance.tag.all():
		tag_ids.append(tag_item.id)
	for item in form.instance.ingredients.all():
		ingredient = Ingredient.objects.get(id=item.ingredient_id)
		# import pdb; pdb.set_trace()
		ingredients.append({'id': ingredient.id, 'name': ingredient.name, 'quantity': item.quantity, 'units': ingredient.units})

	return render(request, 'formChangeRecipe.html', {'form': form, 'tags': tag_ids, 'ingredients': ingredients})

from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import View

def favourites(request):
	user = request.user
	recipes = user.fav_recipes.all()
	return render(request, 'favorite.html', {'recipes': recipes})

class FavouritesView(View):
	def get(self, request):
		import pdb; pdb.set_trace()
		# cart = Cart(request)
		# print(cart.__dict__)
		# res = []
		# for val in cart.cart.values():
		#     res.append(val)
		return render(request, 'favorite.html')

	def post(self, request, id):		
		recipe = get_object_or_404(Recipe, id=id)
		recipe.favourite.add(request.user)
		return JsonResponse({'success': True})

	def delete(self, request, id):
		recipe = Recipe.objects.get(id=id)
		recipe.favourite.remove(request.user)
		return JsonResponse({'success': True})


class SubscriptionsView(View):
	def post(self, request):
		# import pdb; pdb.set_trace()
		id = json.loads((request.body).decode('utf8'))['id']
		user = request.user
		author = User.objects.get(id=id)
		follow = Follow.objects.filter(user=user, author=author).exists()
		if(user != author and follow is False):
			follow = Follow.objects.create(user=user, author=author)
			return JsonResponse({'success': True})
		# return redirect('follows') 
		 
		# recipe = get_object_or_404(Recipe, id=id)
		# recipe.favourite.add(request.user)
		return JsonResponse({'success': False})	

	def delete(self, request, id):
		user = request.user
		author = User.objects.get(id=id)
		follow = Follow.objects.get(user=user, author=author)
		follow.delete()
		return JsonResponse({'success': True})