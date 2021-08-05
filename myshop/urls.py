from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from shop import views
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/media/favicon.ico'), name='favicon'),
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('shop/', include(('shop.urls', 'shop'), namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
