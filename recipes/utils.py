from django.shortcuts import get_object_or_404
from recipes.models import Tag, Recipe


def get_tags(request):
    tags = []
    for key in request.POST.getlist('tag'):
        tags.append(get_object_or_404(Tag, id=int(key)))
    return tags


def filtered_recipes(request):
    request.GET = request.GET.copy()
    filters = {tag.value: 'checked' for tag in Tag.objects.all()}
    filters = {
        'breakfast': 'checked',
        'lunch': 'checked',
        'dinner': 'checked'
        }
    try:
        filters['breakfast'] = (
            'checked' if request.GET['breakfast'] == '1' else ''
        )
        filters['lunch'] = 'checked' if request.GET['lunch'] == '1' else ''
        filters['dinner'] = 'checked' if request.GET['dinner'] == '1' else ''
    except MultiValueDictKeyError:
        pass


    res = []
    recipes = Recipe.objects.all()
    for recipe in recipes:
        for tag in recipe.taglist:
            if recipe not in res:
                if (
                    tag.id == 1 and filters['breakfast'] == 'checked'
                    or tag.id == 2 and filters['lunch'] == 'checked'
                    or tag.id == 3 and filters['dinner'] == 'checked'
                ):
                    res.append(recipe)
    return res