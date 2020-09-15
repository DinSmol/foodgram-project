from django.shortcuts import render
from users.forms import LoginForm, UserEditForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from recipes.models import Recipe, Follow
from ingredients.models import Ingredient
from django.contrib.auth.models import User


def index(request):
    if request.method == "POST":
        values = request.POST.getlist('checked[]')
        import pdb; pdb.set_trace()
    recipes = Recipe.objects.all().order_by('-created')
    # import pdb; pdb.set_trace()
    return render(request, 'recipes.html', {'recipes': recipes})

def user_profile(request, id):
    author = User.objects.get(id=id)
    recipes = Recipe.objects.filter(author=author).order_by('-created')
    # import pdb; pdb.set_trace()
    return render(request, 'authorRecipe.html', {'recipes': recipes, 'author': author})
# def index(request):
#     ingredients = Ingredient.objects.all()
#     return  {'ingredients': ingredients}

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
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
    return render(request,'changePassword.html', {'user_form': user_form})

def follows(request):
    # import pdb; pdb.set_trace()
    res = {}
    recipes = []
    user = request.user
    follow = Follow.objects.filter(user=user)
    print(follow)
    if follow:
        authors = [item.author for item in follow]
        # # import pdb; pdb.set_trace()
        # for author in authors:
        #     res[author] = Recipe.objects.filter(author=author)
        #     recipes.append(res)
        #     res = {}
        
        return render(request, 'myFollow.html', {'authors': authors})
    return render(request, 'myFollow.html') 

def user_create(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        import pdb; pdb.set_trace()
        if form.is_valid():
            user = form.save(commit=False)
            # cd = form.cleaned_data
            # user = authenticate(request,
            # username=cd['username'],
            # password=cd['password'])
            print(f'user: {user}')
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

def cart(request):
    return render(request, 'reg.html')

def shoplist(request):
    return render(request, 'shopList.html')


