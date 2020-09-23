import random
import string

from django.shortcuts import get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.text import slugify
from recipes.models import Recipe, Tag


def get_tags(request):
    tags = []
    for key in request.POST.getlist('tag'):
        tags.append(get_object_or_404(Tag, id=int(key)))
    return tags


def get_filters(request):
    request.GET = request.GET.copy()
    filters = {tag.tag_name_eng: 'checked' for tag in Tag.objects.all()}

    for key in filters:
        try:
            filters[key] = (
                'checked' if request.GET[key] == '1' else ''
            )
        except MultiValueDictKeyError:
            pass

    return filters


def filtered_recipes(request):
    filters = get_filters(request)
    tag_names = [k for k, v in filters.items() if v == 'checked']
    recipes = Recipe.objects.filter(tag__tag_name_eng__in=tag_names).distinct()
    return filters, recipes


def random_string_generator(
        size=10,
        chars=string.ascii_lowercase + string.digits
        ):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance):
    slug = slugify(instance.title.lower(), allow_unicode=True)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance)
    return slug


def get_favourites(request):
    user = request.user
    if user.is_authenticated:
        favourite_ids = [item.id for item in user.user_favourites.all()]
        return favourite_ids
    return None
