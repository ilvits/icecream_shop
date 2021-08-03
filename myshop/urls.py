from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from shop import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('shop/', include(('shop.urls', 'shop'), namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
