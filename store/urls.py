
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_categories, name='all_categories'),
    path('my_cart/', views.my_cart, name='my_cart'),
    path('<product_id>/', views.show, name='show'),
    path('add/<product_id>/', views.add_to_cart, name='add_to_cart'),
]