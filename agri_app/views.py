from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from . import views
from .models import Blogs

def index(request):
    blog_content = Blogs.objects.all()    
    
    return render(request, 'index.html', {'blogs' : blog_content})

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['username'];
        email = request.POST['email'];
        password1 = request.POST['password1'];
        password2 = request.POST['password2'];
        
        if password1 == password2:
            user = User.objects.create_user(username=name, email=email, password=password1)
            user.is_staff=False
            user.is_superuser=False
            user.save()
            messages.success(request,'Your account has been created successful')
            return redirect('login')
        
        else:
            messages.warning(request, 'Password Mismatching')
            return redirect('signup')
        
    else:
        form = CreateUserForm()
        return render(request, 'signup.html', {'form': form})

def login(request):
    return render(request, 'login.html')


def blogs(request):
    blog_content = Blogs.objects.all()    
    
    return render(request, 'blogs.html', {'blogs' : blog_content})

