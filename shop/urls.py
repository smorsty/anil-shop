from django.contrib import admin
from django.urls import path, include
from shop import views
from django.views.generic import TemplateView


urlpatterns = [

    path("checkout", views.checkout, name="shop/checkout"),
    path("cart", views.cart_view, name="shop/cart"),
    #path("shop", views.shop, name="shop/shop"),
    path("shop", views.ProductsListView.as_view(), name='shop/shop'),#(template_name='shop/shop.html')
    path("wishlist", views.wishlist, name="shop/wishlist"),
    path('product/<int:pk>', views.ProductsDetailView.as_view(), name='shop/product_details'),
    path('add_item_to_cart/<int:pk>', views.add_item_to_cart, name='add_item_to_cart'),

]