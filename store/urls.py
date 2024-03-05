from django.urls import path
from . import views
from .views import ListCategories, DetailProduct

urlpatterns = [
    path('', ListCategories.as_view(), name='all_categories'),
    path('create_order/', views.create_order, name='create_order'),
    path('products/<slug:category_slug>/', views.products_category, name='products_category'),
    path('product/<slug:slug>/', DetailProduct.as_view(), name='view_product'),
]