from django.urls import path
from django.conf.urls import include
from .views import SignUpView, UserProfile

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserProfile.as_view(), name='profile'),
]