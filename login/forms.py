from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=5)
