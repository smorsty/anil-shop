from django.shortcuts import render, redirect
from django.contrib.auth import logout

#AUNTHENTICATION


def login_user(request):
    return render(request, "authentication/login.html")

def register(request):
    return render(request, "authentication/register.html")

def logout_user(request):
    logout(request)
    return redirect('index')
