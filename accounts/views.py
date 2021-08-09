from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404
from orders.models import Order
from shop.views import Category
from .forms import UserCreateForm

@login_required
def order_detail(request, order_id):
    categories = Category.objects.all()
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'order/order_detail.html',
                  {'order': order, 'categories': categories})


class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'

@login_required
def user_profile(request):
    user = None
    user = request.user
    if user.is_superuser:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(owner=user.id)
    return render(request,
                  'user_profile.html',
                  {'orders': orders})

