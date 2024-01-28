from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('my_cart/', views.my_cart, name='my_cart'),
    path('my_cart/<int:product_id>/', views.delete_all, name='delete_all'),
    path('my_cart/unit/<int:product_id>/', views.delete_unit, name='delete_unit')
]