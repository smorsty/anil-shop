from django.contrib import admin
from django.urls import path, include
from shop import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path("shop", views.shop, name="shop/shop"),
    path("shop/men", views.shop_men, name="shop/shop/men"),

    path("shop/men/polo_ralph_lauren", views.shop_men_polo_ralph_lauren, name="shop/shop/men/polo_ralph_lauren"),
    path("shop/men/hugo_boss", views.shop_men_hugo_boss, name="shop/shop/men/hugo_boss"),
    path("shop/men/tommy_hilfiger", views.shop_men_tommy_hilfiger, name="shop/shop/men/tommy_hilfiger"),
    path("shop/men/tommy_jeans", views.shop_men_tommy_jeans, name="shop/shop/men/tommy_jeans"),
    path("shop/men/marco_polo", views.shop_men_marco_polo, name="shop/shop/men/marco_polo"),
    path("shop/men/calvin_klein", views.shop_men_calvin_klein, name="shop/shop/men/calvin_klein"),
    path("shop/men/marco_di_radi", views.shop_men_marco_di_radi, name="shop/shop/men/marco_di_radi"),

    path("shop/men/nike", views.shop_men_nike, name="shop/shop/men/nike"),
    path("shop/men/nike_sb", views.shop_men_nike_sb, name="shop/shop/men/nike_sb"),
    path("shop/men/adidas", views.shop_men_adidas, name="shop/shop/men/adidas"),
    path("shop/men/adidas_originals", views.shop_men_adidas_originals, name="shop/shop/men/adidas_originals"),
    path("shop/men/converse", views.shop_men_converse, name="shop/shop/men/converse"),
    path("shop/men/new_balance", views.shop_men_new_balance, name="shop/shop/men/new_balance"),
    path("shop/men/reebok", views.shop_men_reebok, name="shop/shop/men/reebok"),
    path("shop/men/puma", views.shop_men_puma, name="shop/shop/men/puma"),

    path("shop/men/the_north_face", views.shop_men_the_north_face, name="shop/shop/men/the_north_face"),
    path("shop/men/jordan", views.shop_men_jordan, name="shop/shop/men/jordan"),
    path("shop/men/sporty_rich", views.shop_men_sporty_rich, name="shop/shop/men/sporty_rich"),
    path("shop/men/massimo_duti", views.shop_men_massimo_duti, name="shop/shop/men/massimo_duti"),
    path("shop/men/zara", views.shop_men_zara, name="shop/shop/men/zara"),
    path("shop/men/hm", views.shop_men_hm, name="shop/shop/men/hm"),
    path("shop/men/levis", views.shop_men_levis, name="shop/shop/men/levis"),
    path("shop/men/oysho", views.shop_men_oysho, name="shop/shop/men/oysho"),

    path("shop/men/polo_assn", views.shop_men_polo_assn, name="shop/shop/men/polo_assn"),
    path("shop/men/mango", views.shop_men_mango, name="shop/shop/men/mango"),
    path("shop/men/timberland", views.shop_men_timberland, name="shop/shop/men/timberland"),
    path("shop/men/ugg", views.shop_men_ugg, name="shop/shop/men/ugg"),
    path("shop/men/cos", views.shop_men_cos, name="shop/shop/men/cos"),
    path("shop/men/crocs", views.shop_men_crocs, name="shop/shop/men/crocs"),




    path("shop/women", views.shop_women, name="shop/shop/women"),
    path("shop/accessories", views.shop_accessories, name="shop/shop/accessories"),

    #path('shop', views.ProductsListView.as_view(), name='shop/shop'),#(template_name='shop/shop.html')
    path("checkout", views.checkout, name="shop/checkout"),
    path("cart", views.cart_view, name="shop/cart"),
    path("wishlist", views.wishlist, name="shop/wishlist"),
    path('product/<int:pk>', views.ProductsDetailView.as_view(), name='shop/product_details'),
    path('add_item_to_cart/<int:pk>', views.add_item_to_cart, name='add_item_to_cart'),
    path('delete_item/<int:pk>', views.CartDeleteItem.as_view(), name='cart_delete_item'),
    path('make_order/', views.make_order, name='make_order'),

]


urlpatterns += static(settings.MEDIA_URL, documetn_root=settings.MEDIA_ROOT)
