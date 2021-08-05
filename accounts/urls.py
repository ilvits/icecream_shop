from django.urls import path
from django.conf.urls import url, include
from .views import SignUpView
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    url(r'^profile/', views.user_profile, name='user_profile'),
	url(r'^order/(?P<order_id>[-\w]+)/$', views.order_detail, name='order_detail'),
]