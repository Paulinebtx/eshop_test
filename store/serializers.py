from rest_framework import serializers
from .models import Category
from .models import Product


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
