from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password)
        return redirect('index')
    else:
        user_form = UserForm()
        return render(request, 'login/signup_form.html', {'user_form': user_form})
        
def signin(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return HttpResponse('Return an invalid login error message')
    else:
        user_form = UserForm()
        return render(request, 'login/signin_form.html', {'user_form': user_form})
