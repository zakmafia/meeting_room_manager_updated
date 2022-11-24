from django.shortcuts import render, redirect
from datetime import datetime

current_year = datetime.now().year

def home(request):
    context = {
        'current_year': current_year,
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'current_year': current_year
    }
    return render(request, 'about.html', context)