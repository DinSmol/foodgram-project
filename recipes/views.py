from django.shortcuts import render
from recipes.forms import IngredientForm
from ingredients.models import Ingredient
from ingredients.views import get_ingredients
from recipes.models import Recipe
from django.views.decorators.http import require_POST
import json
from .forms import RecipeForm


# Create your views here.
def new(request):
    if request.method == 'POST':
        ingredients = get_ingredients(request)
        tags = get_tags(request)
        form = RecipeForm(request.POST, files=request.FILES or None)
        import pdb; pdb.set_trace()
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            
            return redirect('index')
    else:
        form = RecipeForm()
        tags = {'Завтрак': 'Завтрак','Обед': 'Обед', 'Ужин': 'Ужин'}
    import pdb; pdb.set_trace()
    return render(request, 'formRecipe.html', {'form': form, 'tags': tags})


def purchases(request):
    id = json.loads((request.body).decode('utf8'))['id']
    lst = Recipe.objects.get(id=id)
    print(lst.title)
    return render(request, 'shopList.html')


def get_tags(request):
    tags = []
    if 'breakfast' in request.POST.keys():
        tags.append('Завтрак')
    if 'lunch' in request.POST.keys():
        tags.append('Обед')
    if 'dinner' in request.POST.keys():
        tags.append('Ужин')
    return tags