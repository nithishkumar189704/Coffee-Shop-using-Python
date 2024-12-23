from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee

def homepage(request):
    coffee = Coffee.objects.all()
    return render(request, 'homepage.html', {'coffee': coffee})

