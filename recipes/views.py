from django.shortcuts import render
from recipes.forms import IngredientForm
from ingredients.models import Ingredient
from recipes.models import Recipe
from django.views.decorators.http import require_POST
import json
from cart.views import PurcasesView


# Create your views here.
def new(request):
    form = IngredientForm()
    options = Ingredient.objects.all()
    return render(request, 'formRecipe.html', {
        'form': form, 
        'options': options,
    })


def purchases(request):
    id = json.loads((request.body).decode('utf8'))['id']
    PurcasesView(request, id)
    lst = Recipe.objects.get(id=id)
    print(lst.title)
    return render(request, 'shopList.html')


