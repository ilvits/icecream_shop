from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404
from orders.models import Order
from django.contrib.auth import get_user_model
from .forms import UserCreateForm


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'order/order_detail.html',
                  {'order': order})


class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserProfile(generic.ListView):

    model = Order
    context_object_name = 'order_list'   # ваше собственное имя переменной контекста в шаблоне
    queryset = Order.objects.all() # Получение объектов
    template_name = 'profile.html'  # Определение имени вашего шаблона и его расположения

    # def get(self, request):
    #     if request.user.is_authenticated():
    #         user = request.user.username
    #         return render(request, 'profile.html', {'user': user})

