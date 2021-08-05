from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404
from orders.models import Order
from .forms import UserCreateForm


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'order/order_detail.html',
                  {'order': order})


class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'


def user_profile(request):
    user = request.user
    if user == 'ilvits':
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(owner=user.id)
    return render(request,
                  'user_profile.html',
                  {'orders': orders})

