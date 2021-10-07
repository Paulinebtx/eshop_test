from rest_framework import serializers
from .models import Basket
from .models import Basket_item, Address
from django.contrib.auth.models import User


class AddressSerializer(serializers.Serializer):

    class Meta:
        model = Address
        fields = "__all__"


class basketSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Basket
        fields = ('__all__')
        read_only_fields = ['user']


class basket_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket_item
        fields = ('__all__')


class UserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = "__all__"
