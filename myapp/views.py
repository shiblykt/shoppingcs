from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import gallery

def index(request):
    gals = gallery.objects.all()
    return render(request,'index.html',{'gals':gals})

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def forgotpassword(request):
    return render(request,'forgotpassword.html')

def otp(request):
    return render(request,'otp.html')

def signup(request):
    if request.method == 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username  Already Exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password2)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not the same')
            return redirect('signup')
            
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'invalid credentials')
            return redirect(request,'login.html')
    else:
        return render(request,'login.html')

# Create your views here.
