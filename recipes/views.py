from django.shortcuts import render
from recipes.forms import IngredientForm
from ingredients.models import Ingredient
from ingredients.views import get_ingredients
from recipes.models import Recipe
from django.views.decorators.http import require_POST
import json
from .forms import RecipeForm
from django.shortcuts import redirect
from recipes.models import Tag

# Create your views here.
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
    for tag_item in form.instance.tag.all():
        tag_ids.append(tag_item.id)

    return render(request, 'formChangeRecipe.html', {'form': form, 'tags': tag_ids})