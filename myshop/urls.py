from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from shop import views
from django.views.generic import RedirectView

urlpatterns = [
                  path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'favicon/favicon.png')),
                  path('admin/', admin.site.urls),
                  path('', views.homepage, name='homepage'),
                  path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
                  path('accounts/', include('allauth.urls')),
                  path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
                  path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
                  path('shop/', include(('shop.urls', 'shop'), namespace='shop')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
