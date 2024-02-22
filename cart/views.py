from django.shortcuts import render, HttpResponse, redirect
from store.models import Product, User, CartItem, Category, Cart
from django.contrib import messages
from django.urls import reverse
from django.db.models import F

# Create your views here.

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect(reverse('signin'))
    else:
        cart_obj, cart_create = Cart.objects.get_or_create(user = request.user)
        product = Product.objects.get(id=product_id)
        cartitem, cartitem_create = CartItem.objects.get_or_create(cart=cart_obj, product=product)
        if CartItem.objects.contains(cartitem):
            CartItem.objects.filter(product=product).update(quantity=F('quantity') + 1)
        messages.success(request, "Product add to cart!")
        return redirect(reverse('products_category', args=(product.category.id,)))

def my_cart(request):
    if not request.user.is_authenticated:
        return redirect(reverse('signin'))
    else:
        my_cart = Cart.objects.get(user=request.user.id)    
        products_cart = CartItem.objects.filter(cart=my_cart.id)
        total = sum([product.total_price() for product in products_cart])
        return render(request, 'cart/my_cart.html', {'products_cart': products_cart, 'total': total})

def delete_all(request, product_id):
    CartItem.objects.get(id=product_id).delete()
    return redirect(reverse('my_cart'))

def delete_unit(request, product_id):
    product = CartItem.objects.get(id=product_id)
    if product.quantity <= 1:
        delete_all(request, product_id)
        return redirect(reverse('my_cart'))
    else:
        CartItem.objects.filter(id=product_id).update(quantity=F('quantity') - 1)
        return redirect(reverse('my_cart'))