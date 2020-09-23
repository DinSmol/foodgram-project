from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from recipes.models import Follow, Recipe
from recipes.utils import filtered_recipes, get_favourites
from users.forms import CreationForm

from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from cart.cart import Cart
from cart.utils import get_cart_ids


class SignUp(CreateView):
    form_class = CreationForm
    success_url = "/auth/login/"
    template_name = "signup.html"


def index(request):
    request.GET = request.GET.copy()
    cart_ids = get_cart_ids(request)
    favourite_ids = get_favourites(request)
    filters, recipes = filtered_recipes(request)
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
    return render(request, 'recipes.html', context)


def user_profile(request, id):
    author = get_object_or_404(User, id=id)
    recipes = Recipe.objects.filter(author=author)
    try:
        follow = Follow.objects.filter(user=request.user, author=author)[0]
    except IndexError:
        follow = ''
    return render(
        request,
        'authorRecipe.html',
        {'recipes': recipes, 'author': author, 'follow': follow}
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
