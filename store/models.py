from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import datetime


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, default='admin', null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', default='images/default.png', null=True)
    slug = models.SlugField(max_length=255, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    in_stock = models.BooleanField(default=True, null=True)
    is_active = models.BooleanField(default=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    users_wishlist = models.ManyToManyField(User, related_name='product', blank=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
