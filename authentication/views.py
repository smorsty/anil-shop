from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from authentication.forms import LoginForm, RegisterForm
from django.views.generic import TemplateView

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


class RegisterView(TemplateView):
    template_name = 'authentication/register.html'

    def get(self, request):
        user_form = RegisterForm()
        context = {'user_form': user_form}
        return render(request, "authentication/register.html", context)

    def post(self, request):
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save() # создание нового пользователя
            user.set_password(user.password) # сохраняем хеш пароль, а не сам пароль, одностороняя функция
            user.save() #добавление в БД
            login(request, user)
            return redirect('index')

        context = {'user_form': user_form}
        return render(request, "authentication/register.html", context)



def logout_user(request):
    logout(request)
    return redirect('index')
