from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from recipes.models import Recipe
from .cart import Cart
from rest_framework import status


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Recipe, id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')

# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Recipe, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    # import pdb; pdb.set_trace()
    print(cart.__dict__)
    res = []
    for val in cart.cart.values():
        res.append(val)
    # import pdb; pdb.set_trace()
    return render(request, 'shopList.html', {'cart': res})


from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from rest_framework.permissions import IsAuthenticated

# from .models import Article
# from .serializers import ArticleSerializer

def purchases(request, *args, **kwargs):
    import pdb; pdb.set_trace()
    if request.method == 'GET':
        cart = Cart(request)
        print(cart.__dict__)
        res = []
        for val in cart.cart.values():
            res.append(val)
        return render(request, 'shopList.html', {'cart': res})

    if request.method == 'POST':
        id = json.loads((request.body).decode('utf8'))['id']
        cart = Cart(request)
        product = get_object_or_404(Recipe, id=id)
        cart.add(product=product)
        res = []
        for val in cart.cart.values():
            res.append(val)
        return render(request, 'shopList.html', {'cart': res}) 
    
    if request.method == 'DELETE':
        id = request.resolver_match.kwargs.get('id')
        cart = Cart(request)
        cart.remove(id)
        res = []
        for val in cart.cart.values():
            res.append(val)
        return render(request, 'shopList.html', {'cart': res})

# def purchases_del(request, *args, **kwargs):
#     id = json.loads((request.body).decode('utf8'))['id']
#     cart = Cart(request)
#     cart.remove(id)
#     return render(request, 'shopList.html', {'cart': res})
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import View


class PurchasesView(View):
    def get(self, request):
        cart = Cart(request)
        print(cart.__dict__)
        res = []
        for val in cart.cart.values():
            res.append(val)
        return render(request, 'shopList.html', {'cart': res})

    def post(self, request, id):
        recipe_id = json.loads(request.body).get('id')
        recipe = get_object_or_404(Recipe, id=recipe_id)
        cart = Cart(request)
        cart.add(product=recipe)
        return JsonResponse({'success': True})

    def delete(self, request, id):
        recipe = Recipe.objects.get(id=id)
        cart = Cart(request)
        cart.remove(id)
        return JsonResponse({'success': True})

    # def get(self, request):
    #     cart = Cart(request)
    #     print(cart.__dict__)
    #     res = []
    #     for val in cart.cart.values():
    #         res.append(val)
    #     return render(request, 'shopList.html', {'cart': res})

    # def post(self, request, *args, **kwargs):
    #     id = request.data.get('id')
    #     cart = Cart(request)
    #     product = get_object_or_404(Recipe, id=id)
    #     cart.add(product=product)
    #     res = []
    #     for val in cart.cart.values():
    #         res.append(val)
    #     messages.success(request, 'Recipe added successfully')
    #     return Response(status=status.HTTP_201_CREATED) 


    # def delete(self, request, *args, **kwargs):
    #     id = kwargs.get('id')
    #     cart = Cart(request)
    #     cart.remove(id)
    #     return Response(status=status.HTTP_204_NO_CONTENT) 
