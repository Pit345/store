from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_categories, name='all_categories'),
    path('products/<slug:category_slug>/', views.products_category, name='products_category'),
    path('product/<int:product_id>/', views.view_product, name='view_product')
]