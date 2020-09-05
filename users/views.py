from django.shortcuts import render
from users.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    if request.user.is_anonymous:
        return render(request, 'indexNotAuth.html')
    # category = None
    # categories = Category.objects.all()
    # products = Product.objects.filter(available=True)
    
    # if category_slug:
    #     category = get_object_or_404(Category, slug=category_slug)
    #     products = products.filter(category=category)

    return render(request, 'indexAuth.html')

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