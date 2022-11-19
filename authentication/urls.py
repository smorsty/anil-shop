from django.contrib import admin
from django.urls import path, include
from authentication import views

#AUTHENTICATION

urlpatterns = [

    path("login", views.login_user, name="authentication/login"),
    path("register", views.RegisterView.as_view(), name="authentication/register"),
    path("logout", views.logout_user, name="authentication/logout"),

]