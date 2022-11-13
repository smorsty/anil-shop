from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from authentication.forms import LoginForm

#AUNTHENTICATION

def login_user(request):
    context = {'login_form': LoginForm()}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                context ={
                    'login_form': LoginForm()
                }
        else:
            context = {
                'login_form': login_form,
            }

    return render(request, "authentication/login.html", context)


def register(request):
    return render(request, "authentication/register.html")

def logout_user(request):
    logout(request)
    return redirect('index')
