from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import feature

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def signup(request):
    if request.method == 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']

        if password == password2:
            if user.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('signup')
            elif user.objects.filter(username=username).exists():
                messages.info(request, 'username  Already Exists')
                return redirect('signup')
            else:
                user = user.objects.create_user(username=username,email=email,password=password2)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not the same')
            return redirect('signup')
            
    return render(request,'signup.html')

# Create your views here.
