from django.conf import settings
from recipes.models import Recipe


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        product_document = {
            'id': product.id,
            'title': product.title,
            'cooking_duration': product.cooking_duration
            }
        if product_id not in self.cart:
            self.cart[product_id] = product_document
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Recipe.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            yield item

    def __len__(self):
        return len(self.cart)

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
