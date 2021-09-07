from django.contrib import admin

from .models import Basket, Basket_item


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Basket_item)
class Basket_itemAdmin(admin.ModelAdmin):
    list_display = ['product', 'date_add', 'basket']
