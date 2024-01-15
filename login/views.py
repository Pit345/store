from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password)
        return redirect('all_categories')
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
            if user:
                login(request, user)
                return redirect(reverse('all_categories'))
            else:
                return HttpResponse(f"User not found. Please sign up!")
    else:
        user_form = UserForm()
        return render(request, 'login/signin_form.html', {'user_form': user_form})

def logout_view(request):
    logout(request)
    redirect(reverse('all_categories'))
    return HttpResponseRedirect('/')
