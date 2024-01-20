from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_categories, name='all_categories'),
    path('products/<str:category_url>/', views.products_category, name='products_category'),
    path('product/<int:product_id>/', views.view_product, name='view_product'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('my_cart/', views.my_cart, name='my_cart'),

]