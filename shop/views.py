from django.shortcuts import render


def checkout(request):
    return render(request, "shop/checkout.html")

def cart(request):
    return render(request, "shop/cart.html")

def shop(request):
    return render(request, "shop/shop.html")

def wishlist(request):
    return render(request, "shop/wishlist.html")
