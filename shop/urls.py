from django.contrib import admin
from django.urls import path, include
from shop import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path("checkout", views.checkout, name="shop/checkout"),
    path("cart", views.cart_view, name="shop/cart"),
    #path("shop", views.shop, name="shop/shop"),
    path("shop", views.ProductsListView.as_view(), name='shop/shop'),#(template_name='shop/shop.html')
    path("wishlist", views.wishlist, name="shop/wishlist"),
    path('product/<int:pk>', views.ProductsDetailView.as_view(), name='shop/product_details'),
    path('add_item_to_cart/<int:pk>', views.add_item_to_cart, name='add_item_to_cart'),
    path('delete_item/<int:pk>', views.CartDeleteItem.as_view(), name='cart_delete_item'),
    path('make-order/', views.make_order, name='make_order'),

]


urlpatterns += static(settings.MEDIA_URL, documetn_root=settings.MEDIA_ROOT)
