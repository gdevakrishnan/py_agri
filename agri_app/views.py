from django.shortcuts import render
from . import views

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def about(request):
    return render(request, 'about.html')
