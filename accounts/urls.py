from django.urls import include, path

urlpatterns = [
    path('', include('django_registration.backends.activation.urls')),
    path('', include('django.contrib.auth.urls')),
]