from rest_framework import serializers
from .models import Basket
from .models import Basket_item


class basketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('__all__')


class basket_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket_item
        fields = ('__all__')
