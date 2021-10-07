from rest_framework import viewsets
from .serializers import basketSerializer
from .serializers import basket_itemSerializer, AddressSerializer
from .models import Basket
from .models import Basket_item, Address


class AddressViewsets(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class BasketViewsets(viewsets.ModelViewSet):
    serializer_class = basketSerializer
    queryset = Basket.objects.all()


class Basket_itemViewsets(viewsets.ModelViewSet):
    serializer_class = basket_itemSerializer
    queryset = Basket_item.objects.all()
