from .cart import Cart


def cart(request):
    user = request.user
    return {'cart': Cart(request), 'user': user}
