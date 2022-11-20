from django.contrib import admin
from django.urls import path, include
from shop import views
from django.views.generic import TemplateView


urlpatterns = [

    path("checkout", views.checkout, name="shop/checkout"),
    path("cart", views.cart, name="shop/cart"),
    path("shop", views.shop, name="shop/shop"),
    path("wishlist", views.wishlist, name="shop/wishlist"),
    path('product/<int:pk>',
        TemplateView.as_view(template_name='shop/product_details.html'),
        name='shop/product_details'),
    # <int:pk> -> плюшка, для каждого продукта своя ссылка по идее
    # плюс новая структура передачи ссылки

]