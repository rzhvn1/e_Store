from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm
from django.contrib.auth.models import User

# Create your views here.
# здесь происходит наша основная логика нашего сайта

def products_page(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {"products":products})

def order_page(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'products/order.html', {"form":form})

def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'products/register.html', {"form":form})

def all_users_page(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'products/all_user.html', context)

def about_us_page(request):
    about_us = AboutUs.objects.all()
    context = {'about_us':about_us}
    return render(request, 'products/about_us.html', context)