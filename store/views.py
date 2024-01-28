from django.shortcuts import render, HttpResponse, redirect
from store.models import Product, User, CartItem, Category, Cart
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'store/categories.html', {'categories': categories})

def products_category(request, category_url):
    category_name = category_url.replace('-', ' ')
    category = Category.objects.get(name=category_name)
    products = category.product_set.all()
    return render(request, 'store/products_category.html', {'products': products})
    
def view_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/view_product.html', {'product': product})