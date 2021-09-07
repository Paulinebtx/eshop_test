from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from basket.viewsets import BasketViewsets, Basket_itemViewsets
from store.viewsets import ProductViewsets, CategoryViewsets


router = routers.DefaultRouter()
router.register(r'basket', BasketViewsets, 'basket')
router.register(r'basket_item', Basket_itemViewsets, 'basket_item')
# all products:
router.register(r'product', ProductViewsets, 'product')
# all categories:
router.register(r'category', CategoryViewsets, 'category')


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('store/', include('store.urls', namespace='store')),
    # path('basket/', include('basket.urls', namespace='basket')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
