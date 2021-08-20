from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .tasks import send_contact_form

from .models import Category, Product

from cart.forms import CartAddProductForm


def homepage(request):
    return render(request, 'shop/home.html')


def test(request):
    return render(request, 'shop/test.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products}
                  )


# @login_required
# def product_detail(request, product_id, slug):
#     product = get_object_or_404(Product,
#                                 product_id=product_id,
#                                 slug=slug,
#                                 available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'shop/product/detail.html', {'product': product,
#                                                         'cart_product_form': cart_product_form})


def contact_form(request):
    user = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    if request.method == 'POST':
        send_contact_form.delay(user, email, message)
        messages.success(request, 'Ваше сообщение отправлено!')
        return render(request, 'shop/contact.html',
                      {'message': message})

    else:
        return render(request, 'shop/contact.html')
