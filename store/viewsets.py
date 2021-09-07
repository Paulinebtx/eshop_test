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


class Product_deleteViewsets(viewsets.ModelViewSet):
    model = Product
    context_object_name = 'Product'
    queryset = Product.objects.all()
    serializer_class = productSerializer

    def delete(request, id):
        context = {}
        obj = get_object_or_404(Product, id=id)

        if request.method == "POST":
            # delete object
            obj.delete()
            return HttpResponseRedirect("/")


class CategoryViewsets(viewsets.ModelViewSet):
    serializer_class = categorySerializer
    queryset = Category.objects.all()
