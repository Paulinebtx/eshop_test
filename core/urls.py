from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from basket.viewsets import BasketViewsets, Basket_itemViewsets
from authuser import views as userview
from store.viewsets import ProductViewsets, CategoryViewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/register', userview.UserCreate.as_view()),
    path('api/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
