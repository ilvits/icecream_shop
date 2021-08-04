from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404
from orders.models import Order
from django.contrib.auth import get_user_model


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserProfile(generic.ListView):
    model = Order
    context_object_name = 'order_list'   # ваше собственное имя переменной контекста в шаблоне
    queryset = Order.objects.all()[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'profile.html'  # Определение имени вашего шаблона и его расположения

    # def get(self, request):
    #     if request.user.is_authenticated():
    #         user = request.user.username
    #         return render(request, 'profile.html', {'user': user})
