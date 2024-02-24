from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=250, db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=1_000_000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price

class Order(models.Model):

    PAYMENT_METHOD = [
        ('cash_courier', 'Наличными курьеру'),
        ('card_courier', 'Картой курьеру'),
        ('card_online', 'Картой онлайн'),]

    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=1_000_000)
    quantity = models.PositiveIntegerField(default=1)