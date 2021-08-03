from django.urls import path
from django.conf.urls import include
from .views import SignUpView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
]