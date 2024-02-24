from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from store.models import Product, User, CartItem, Category, Cart
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .forms import OrderForm
from .models import *

# Create your views here.

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'store/categories.html', {'categories': categories})

def products_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.product_set.all()
    return render(request, 'store/products_category.html', {'products': products})
    
def view_product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    return render(request, 'store/view_product.html', {'product': product})

def create_order(request):
    if request.method == 'GET':
        order_form = OrderForm()
        return render(request, 'store/create_order.html', {'order_form': order_form})
    else:
        cart = get_object_or_404(Cart, user=request.user)
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = Order.objects.create(name=order_form.cleaned_data.get('name'),
                                        phone_number=order_form.cleaned_data.get('phone_number'),
                                        payment_method=order_form.cleaned_data.get('payment_method'),
                                        user = request.user)
            
            for cart_item in cart.cartitem_set.all():
                OrderItem.objects.create(order=order, product=cart_item.product, 
                                         quantity = cart_item.quantity, price=cart_item.product.price)

            return redirect(reverse('my_cart'))