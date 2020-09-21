import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from ingredients.views import get_ingredients
from recipes.models import Follow, Recipe, Tag

from .forms import RecipeForm


def new(request):
    if request.method == 'POST':
        ingredients = get_ingredients(request)
        tags = get_tags(request)
        form = RecipeForm(request.POST, files=request.FILES or None)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            for tag in tags:
                recipe.tag.add(tag)
            for item in ingredients:
                recipe.ingredients.add(item.id)
            return redirect('index')
    else:
        form = RecipeForm()
        tags = {'Завтрак': 'Завтрак', 'Обед': 'Обед', 'Ужин': 'Ужин'}
    return render(request, 'formRecipe.html', {'form': form, 'tags': tags})


def recipe_delete(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return redirect('index')


def purchases(request):
    id = json.loads(request.body)['id']
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'shopList.html')


def get_tags(request):
    tags = []
    for key in request.POST.getlist('tag'):
        tags.append(get_object_or_404(Tag, id=int(key)))
    return tags


def recipe_change(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':
        ingredients = get_ingredients(request)
        tags = get_tags(request)
        form = RecipeForm(
            request.POST,
            instance=recipe,
            files=request.FILES or None
        )
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            recipe.tag.clear()
            recipe.ingredients.clear()

            for tag in tags:
                recipe.tag.add(tag)
            for item in ingredients:
                recipe.ingredients.add(item)
            return redirect('index')

    tags = [tag.id for tag in recipe.taglist]
    ingredients = recipe.ingredientlist
    form = RecipeForm(instance=recipe)
    return render(
        request,
        'formChangeRecipe.html',
        {
            'form': form,
            'recipe': recipe,
            'tags': tags,
            'ingredients': ingredients
        }
    )


def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    ingredients = recipe.ingredientlist
    return render(
        request,
        'singlePage.html',
        {'recipe': recipe, 'ingredients': ingredients}
    )


def favourites(request):
    user = request.user
    recipes = user.fav_recipes.all()
    return render(request, 'favorite.html', {'recipes': recipes})


class FavouritesView(View):
    http_method_names = ['get', 'post', 'delete']

    def get(self, request):
        return render(request, 'favorite.html')

    def post(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        recipe.favourite.add(request.user)
        return JsonResponse({'success': True})

    def delete(self, request, id):
        recipe = get_object_or_404Recipe, id=id)
        recipe.favourite.remove(request.user)
        return JsonResponse({'success': True})


class SubscriptionsView(View):
    def post(self, request):
        id = json.loads(request.body)['id']
        user = request.user
        author = get_object_or_404(User, id=id)
        follow = Follow.objects.get_or_create(user=user, author=author)
        return JsonResponse({'success': True})



    def delete(self, request, id):
        user = request.user
        author = get_object_or_404(User, id=id)
        follow = get_object_or_404(Follow, user=user, author=author).delete()
        return JsonResponse({'success': True})
