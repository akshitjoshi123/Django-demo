import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, logout, login
from appAuth import models
from django.contrib import messages

# Create your views here.

def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def registration(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist!')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist!')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
        else:
            messages.info(request, 'Password not match!')
            return redirect('registration')
        return redirect("/")
    else:   
        return render(request, 'registration.html')