from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView.as_view(),  name="product_list"),
    path('<category_slug>', views.ProductView.as_view(),  name="product_list_by_category"),
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
    #     views.product_detail,
    #     name='product_detail'),
]
