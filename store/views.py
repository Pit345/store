from django.shortcuts import render, HttpResponse
from store.models import Product, User, CartItem

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})

def show(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/show.html', {'product': product})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cartitem = CartItem.objects.create(user= request.user, product=product)
    return HttpResponse(f"Пользователь № {cartitem.user_id} add to cart {cartitem.product_id}")

def my_cart(request):   
    products_user = CartItem.objects.filter(user_id=request.user.id)
    return render(request, 'store/my_cart.html', {'products_user': products_user})