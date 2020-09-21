import csv
import json
from io import StringIO

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.views.generic import View
from recipes.models import Recipe

from .cart import Cart


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Recipe, id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Recipe, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    res = cart.cart.values()
    return render(request, 'shopList.html', {'cart': res})


def cart_export(request):
    cart = Cart(request)
    res = cart.cart.values()
    new_csvfile = StringIO.StringIO()

    wr = csv.writer(new_csvfile, quoting=csv.QUOTE_ALL)
    for item in res:
        products = item.ingredientlist
        wr.writerows([[item.title]])
        for product in products:
            wr.writerows(
                [[product.ingredient.name +
                '-' + str(product.quantity) +
                product.ingredient.units]]
            )

    response = HttpResponse(new_csvfile.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=stock.csv'
    return response


def purchases(request, *args, **kwargs):
    if request.method == 'GET':
        cart = Cart(request)
        res = cart.cart.values()
        return render(request, 'shopList.html', {'cart': res})

    if request.method == 'POST':
        id = json.loads((request.body).decode('utf8'))['id']
        cart = Cart(request)
        product = get_object_or_404(Recipe, id=id)
        cart.add(product=product)
        res = cart.cart.values()
        return render(request, 'shopList.html', {'cart': res})

    if request.method == 'DELETE':
        id = request.resolver_match.kwargs.get('id')
        cart = Cart(request)
        cart.remove(id)
        res = cart.cart.values()
        return render(request, 'shopList.html', {'cart': res})


class PurchasesView(View):
    def get(self, request):
        cart = Cart(request)
        res = []
        for recipe_id in cart.cart.keys():
            res.append(get_object_or_404(Recipe, id=recipe_id))
        return render(request, 'shopList.html', {'cart': res})

    def post(self, request, id):
        recipe_id = json.loads(request.body).get('id')
        recipe = get_object_or_404(Recipe, id=recipe_id)
        cart = Cart(request)
        cart.add(product=recipe)
        return JsonResponse({'success': True})

    def delete(self, request, id):
        cart = Cart(request)
        cart.remove(id)
        return JsonResponse({'success': True})
