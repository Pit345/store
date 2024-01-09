from django.shortcuts import render, HttpResponse, redirect
from store.models import Product, User, CartItem, Category
from django.contrib import messages

# Create your views here.

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'store/categories.html', {'categories': categories})

def products_category(request):
    ...

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