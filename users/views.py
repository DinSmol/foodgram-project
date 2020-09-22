from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import get_object_or_404

from recipes.models import Follow, Recipe
from recipes.utils import filtered_recipes
from users.forms import CreationForm

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect
from .forms import CreationForm


class SignUp(CreateView):
        form_class = CreationForm
        success_url = "/auth/login/"
        template_name = "signup.html"


def index(request):
    request.GET = request.GET.copy()
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

    recipes = filtered_recipes(filters)
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    request.GET.clear()

    context = {
        'filters': filters,
        'recipes': page,
        'paginator': paginator
        }
    return render(request, 'recipes.html', context)


def user_profile(request, id):
    author = get_object_or_404(User, id=id)
    recipes = Recipe.objects.filter(author=author)
    return render(
        request,
        'authorRecipe.html',
        {'recipes': recipes, 'author': author}
    )


@login_required
def logout(request):
    django_logout(request)
    return redirect('index')


@login_required
def change_password(request):
    if request.method == 'POST':
        user_form = UserEditForm()
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm()
    return render(request, 'changePassword.html', {'user_form': user_form})


def user_create(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'reg.html')


def follows(request):
    user = request.user
    follow = Follow.objects.filter(user=user)
    if follow:
        authors = [item.author for item in follow]
        return render(request, 'myFollow.html', {'authors': authors})
    return render(request, 'myFollow.html')


def shoplist(request):
    return render(request, 'shopList.html')
