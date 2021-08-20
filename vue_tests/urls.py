from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('products/<int:id>/', views.ProductListView.as_view()),
]
