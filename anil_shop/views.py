from django.shortcuts import render

def index(request):
    return render(request, "index/index.html")

#Others Pages

def checkout(request):
    return render(request, "checkout.html")

def cart(request):
    return render(request, "cart.html")

def shop(request):
    return render(request, "shop.html")

def error(request):
    return render(request, "error.html")

def wishlist(request):
    return render(request, "wishlist.html")