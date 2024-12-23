from django.shortcuts import render
from django.http import HttpResponse

def homepage_view(request):
    return render(request, 'homepage.html')

def about_us(request):
    return render(request, 'about_us.html')

def home_view(request):
    return render(request, 'home.html')

def product_view(request):
    return render(request, 'product.html')

def reviews_view(request):
    return render(request, 'reviews.html')

def contact_view(request):
    return render(request, 'contact.html')