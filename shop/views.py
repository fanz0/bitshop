from django.shortcuts import render, redirect
from django.contrib import messages


def home_page(request):
    return render(request, 'shop/home_page.html', {})

def tshirt_details(request):
    return render(request, 'shop/tshirt_details.html', {})

def hoodie_details(request):
    return render(request, 'shop/hoodie_details.html', {})

def payment_details(request):
    return render(request, 'shop/payment_details.html', {})

def index(request):
    messages.success(request, ('The Payment Has Been Successfull'))
    return render(request, 'shop/loading_page.html', {'refresh': 5, 'url': 'home_page'})

