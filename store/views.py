from django.shortcuts import render
from store.models import Product, User, CartItem

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})

def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/detail.html', {'product': product})

def add_to_cart(request, product_id):
    breakpoint()