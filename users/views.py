from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView

from cart.utils import get_cart_ids
from recipes.models import Follow, Recipe
from recipes.utils import filtered_recipes
from users.forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = "/auth/login/"
    template_name = "signup.html"


def index(request):
    request.GET = request.GET.copy()
    cart_ids = get_cart_ids(request)
    filters, recipes = filtered_recipes(request)
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    request.GET.clear()
    context = {
        'cart_ids': cart_ids,
        'filters': filters,
        'recipes': page,
        'paginator': paginator
        }
    return render(request, 'recipes.html', context)


def user_profile(request, id):
    author = get_object_or_404(User, id=id)
    cart_ids = get_cart_ids(request)
    recipes = Recipe.objects.filter(author=author)
    filters, recipes = filtered_recipes(request)
    recipes = recipes.filter(author=author)
    try:
        follow = Follow.objects.filter(user=request.user, author=author)[0]
    except IndexError:
        follow = ''
    return render(
        request,
        'authorRecipe.html',
        {'filters': filters,
        'cart_ids': cart_ids,
        'recipes': recipes,
        'author': author,
        'follow': follow}
    )


@login_required
def logout(request):
    django_logout(request)
    return redirect('index')


def follows(request):
    user = request.user
    follow = Follow.objects.filter(user=user)
    if follow:
        authors = [item.author for item in follow]
        return render(request, 'myFollow.html', {'authors': authors})
    return render(request, 'myFollow.html')


def shoplist(request):
    return render(request, 'shopList.html')
