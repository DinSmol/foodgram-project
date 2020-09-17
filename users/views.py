from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.datastructures import MultiValueDictKeyError
from recipes.models import Follow, Recipe
from users.forms import LoginForm, UserEditForm, UserRegistrationForm


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


def filtered_recipes(filters):
    res = []
    recipes = Recipe.objects.all().order_by('-created')
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


def user_profile(request, id):
    author = User.objects.get(id=id)
    recipes = Recipe.objects.filter(author=author).order_by('-created')
    return render(
        request,
        'authorRecipe.html',
        {'recipes': recipes, 'author': author}
    )


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'])
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
    return render(request, 'authForm.html', {'form': form})


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
