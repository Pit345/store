from django.shortcuts import render, HttpResponse, redirect
from store.models import Product, User, CartItem, Category
from django.contrib import messages

# Create your views here.

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/index.html', {'categories': categories})

def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})

def show(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/show.html', {'product': product})

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        product = Product.objects.get(id=product_id)
        cartitem = CartItem.objects.create(user= request.user, product=product)
        messages.add_message(request, messages.SUCCESS, "Item added to cart")   
        return redirect('index')

def my_cart(request):   
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        products_user = CartItem.objects.filter(user_id=request.user.id)
        return render(request, 'store/my_cart.html', {'products_user': products_user})