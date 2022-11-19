from django.contrib import admin
from django.urls import path, include
from shop import views


urlpatterns = [

    path("checkout", views.checkout, name="shop/checkout"),
    path("cart", views.cart, name="shop/cart"),
    path("shop", views.shop, name="shop/shop"),
    path("wishlist", views.wishlist, name="shop/wishlist"),

]