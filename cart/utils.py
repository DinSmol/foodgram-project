from .cart import Cart


def get_cart_ids(request):
    cart = Cart(request)
    cart_ids = [int(item['id']) for item in cart.cart.values()]
    return cart_ids
