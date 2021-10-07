from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from store.models import Product
from django_countries.fields import CountryField
import datetime


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    street_address = models.CharField(max_length=100)
    number_street = models.CharField(max_length=4)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(blank_label='(select country)')
    zip = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user


class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='user_basket', on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    # ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(Address, related_name='shipping_address',
                                         on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(Address, related_name='billing_address',
                                        on_delete=models.SET_NULL, blank=True, null=True)
    # payment = models.ForeignKey(
    #     'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    # coupon = models.ForeignKey(
    #     'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    def __str__(self):
        return self.user

    def get_total(self):
        total = 0
        for basket_item in self.product.all():
            total += basket_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


class Basket_item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def get_total_item_price(self):
        return self.quantity * self.product.price

    def get_total_discount_item_price(self):
        return self.quantity * self.product.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.product.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

    def __str__(self):
        return self.product
