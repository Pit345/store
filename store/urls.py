
from django.urls import path
from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<product_id>/', views.detail, name='detail'),
    path('add/<product_id>/', views.add_to_cart, name='add_to_cart')
]