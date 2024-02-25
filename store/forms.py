from django.contrib.auth.models import User
from django import forms
from .models import Order

class OrderForm(forms.Form):
    name = forms.CharField(max_length=250)
    phone_number = forms.CharField(max_length=250)
    payment_method = forms.ChoiceField(choices=Order.PAYMENT_METHOD)
