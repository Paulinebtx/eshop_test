from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from store.models import Product


class Basket(models.Model):
    id = models.AutoField(primary_key=True)


class Basket_item(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    basket = models.ForeignKey(Basket, related_name='basket', on_delete=models.CASCADE, null=True)
    # quantity = models.IntegerField(null=False)

    def __str__(self):
        return self.product
