from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def name_to_url(self):
        return self.name.replace(' ', '-')

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=1_000_000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)