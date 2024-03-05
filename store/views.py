from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, CartItem, Category, Cart
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import *
from django.views import generic

# Create your views here.

class ListCategories(generic.ListView):
    model = Category
    template_name = 'store/category_list.html'

def products_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.product_set.all()
    return render(request, 'store/products_category.html', {'products': products})
    
class DetailProduct(generic.DetailView):
    model = Product
    template_name = 'store/view_product.html'

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
                CartItem.objects.filter(product=cart_item.product).delete()

            return redirect(reverse('all_categories'))