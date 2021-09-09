from rest_framework import viewsets
from .serializers import productSerializer
from .serializers import categorySerializer
from .models import Category
from .models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse


class ProductViewsets(viewsets.ModelViewSet):
    serializer_class = productSerializer
    queryset = Product.objects.all()


class CategoryViewsets(viewsets.ModelViewSet):
    serializer_class = categorySerializer
    queryset = Category.objects.all()
