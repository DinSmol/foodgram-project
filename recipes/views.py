from django.shortcuts import render

# Create your views here.
def new_recipe(request):
    return render(request, 'formRecipe.html')

