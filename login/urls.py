from django.urls import path
from login import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', views.signin, name='signin'),
    path('logout/', views.logout_view, name='logout_view')
]