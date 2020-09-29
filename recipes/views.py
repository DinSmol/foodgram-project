import json

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from ingredients.views import get_ingredients

from cart.utils import get_cart_ids
from recipes.models import Follow, Recipe

from .forms import RecipeForm
from .utils import get_favourites, get_filters, get_tags, unique_slug_generator


def new(request):
    if request.method == 'POST':
        ingredients = get_ingredients(request)
        tags = get_tags(request)
        form = RecipeForm(request.POST, files=request.FILES or None)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.slug = unique_slug_generator(recipe)
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


def recipe_change(request, id):
    recipe = get_object_or_404(Recipe, id=id)

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
    favourite_ids = get_favourites(request)
    return render(
        request,
        'singlePage.html',
        {'recipe': recipe,
        'favourite_ids': favourite_ids,}
    )


class FavouritesView(View):
    http_method_names = ['get', 'post', 'delete']

    def get(self, request):
        user = request.user
        filters = get_filters(request)
        tag_names = [k for k, v in filters.items() if v == 'checked']
        cart_ids = get_cart_ids(request)
        favourite_ids = get_favourites(request)
        recipes = user.user_favourites.filter(
            tag__tag_name_eng__in=tag_names).distinct()
        paginator = Paginator(recipes, 6)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        request.GET.clear()

        context = {
            'favourite_ids': favourite_ids,
            'cart_ids': cart_ids,
            'filters': filters,
            'recipes': page,
            'paginator': paginator
            }
        return render(request, 'favorite.html', context)

    def post(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        recipe.favourite.add(request.user)
        return JsonResponse({'success': True})

    def delete(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
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
