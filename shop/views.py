from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView
from shop.forms import AddQuantityForm, CheckoutForm, PickSizeForm, ProductPriceFilterFrom, ProductTypeFilterForm, PickTypeForm
from shop.models import Product, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect
import smtplib
from email.mime.text import MIMEText
from anil_shop.settings import shop_sender, shop_password


def cart(request):
    return render(request, "shop/cart.html")

def wishlist(request):
    return render(request, "shop/wishlist.html")

"""
class ProductsListView(ListView):
    model = Product
    template_name = 'shop/shop.html'
"""

def shop(request):
    products = Product.objects.all()
    form = ProductPriceFilterFrom(request.GET)
    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte больше или равно

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte меньше или равно

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    context = {
        'object_list': products,
        'form': form,
    }
    return render(request, 'shop/shop.html', context)


def shop_men(request):
    products = Product.objects.filter(gender='male')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_polo_ralph_lauren(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Polo Ralph Lauren')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_hugo_boss(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Hugo Boss')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_tommy_hilfiger(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Tommy Hilfiger')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_tommy_jeans(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Tommy jeans')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_marco_polo(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Marco polo')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_calvin_klein(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Calvin Klein')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_marco_di_radi(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Marco di radi')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_nike(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Nike')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_nike_sb(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Nike SB')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_adidas(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Adidas')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_adidas_originals(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Adidas Original')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_converse(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Converse')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_new_balance(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='New Balance')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_reebok(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Reebok')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_puma(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Puma')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_the_north_face(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='The North Face')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_jordan(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Jordan')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_sporty_rich(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Sporty&rich')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_massimo_duti(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Massimo Dutti')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_zara(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Zara')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_hm(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='H&M')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_levis(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Levis')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_oysho(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Oysho')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_polo_assn(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Polo Assn')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_mango(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Mango')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_timberland(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Timberland')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_ugg(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='UGG')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_cos(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Cos')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)

def shop_men_crocs(request):
    products = Product.objects.filter(gender='male')
    products = products.filter(brand='Crocs')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'male'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    if form_product_type.is_valid():
        if form_product_type.cleaned_data['category']:
            products = products.filter(product_type=form_product_type.cleaned_data['category'])


    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,

    }
    return render(request, 'shop/shop.html', context)


def shop_women(request):
    products = Product.objects.filter(gender='female')
    form = ProductPriceFilterFrom(request.GET)
    form_product_type = ProductTypeFilterForm(request.GET)
    gender_check = 'female'
    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

        if form_product_type.is_valid():
            if form_product_type.cleaned_data['category']:
                products = products.filter(product_type=form_product_type.cleaned_data['category'])

    context = {
        'object_list': products,
        'form': form,
        'form_product_type': form_product_type,
        'gender': gender_check,
    }
    return render(request, 'shop/shop.html', context)

def shop_accessories(request):
    products = Product.objects.filter(category='accessories')
    form = ProductPriceFilterFrom(request.GET)
    gender_check = 'accessories'

    if form.is_valid():
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])#price__gte

        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])#price__lte

        if form.cleaned_data['ordering']:
            products = products.order_by(form.cleaned_data['ordering'])

    context = {
        'object_list': products,
        'form': form,
        'gender': gender_check,
    }
    return render(request, 'shop/shop.html', context)
class ProductsDetailView(DetailView):
    model = Product
    template_name = 'shop/product_details.html'


@login_required(login_url=reverse_lazy('authentication/login'))
def add_item_to_cart(request, pk):
    if request.method == 'POST':
        quantity_form = AddQuantityForm(request.POST)
        size_form = PickSizeForm(request.POST)
        if quantity_form.is_valid() and size_form.is_valid():
            quantity = quantity_form.cleaned_data['quantity']
            size = size_form.cleaned_data['size']
            if not size:
                size = 'one_size'
            if quantity:
                cart = Order.get_cart(request.user)
                #product = Product.objects.get(pk=pk)
                product = get_object_or_404(Product, pk=pk)
                cart.orderitem_set.create(product=product,
                                          quantity=quantity,
                                          price=product.price,
                                          size=size,
                                          )
                cart.save()
                return redirect('shop/cart')
        else:
            pass
    return redirect('shop/shop')


@login_required(login_url=reverse_lazy('authentication/login'))
def cart_view(request):
    cart = Order.get_cart(request.user)
    items = cart.orderitem_set.all()
    context = {
        'cart': cart,
        'items': items,
        #'csrfmiddlewaretoken': '{{ csrf_token }}',
    }
    return render(request, 'shop/cart.html', context)


@method_decorator(login_required, name='dispatch')
class CartDeleteItem(DeleteView):
    model = OrderItem
    template_name = 'shop/cart.html'
    success_url = reverse_lazy('shop/cart')


    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(order__user=self.request.user)
        return qs


@login_required(login_url=reverse_lazy('login'))
def make_order(request):
    cart = Order.get_cart(request.user)
    cart.make_order()
    return redirect('shop/shop')


def checkout(request):
    # ���� ����� GET, ������ �����
    if request.method == 'GET':
        form = CheckoutForm()
        cart = Order.get_cart(request.user)
        items = cart.orderitem_set.all()
        context = {
            'form': form,
            'cart': cart,
            'items': items,
        }
    elif request.method == 'POST':
        #settings
        my_recipient = 'demon.am@bk.ru' #main address of our shop
        my_password = "y8nEPsm64q6JVUTwT1gW" #static it's unique for every sender's email
        # �� ���� �� ����� � �� �� ���� �� ����� ����� ������ ������))
        sender = shop_sender
        password = shop_password
        my_recipient = 'diamond.coin@bk.ru'
        shop_recipient = 'anil_shop@mail.ru'
        user_recipient = request.user.email # get users email, for send him a mail with order_information

        # ���� ����� POST, �������� ����� � �������� ������
        form = CheckoutForm(request.POST)
        if form.is_valid():
            #user_information
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            home_number = form.cleaned_data['home_number']
            zip = form.cleaned_data['zip']
            phone = form.cleaned_data['phone']
            comment = form.cleaned_data['comment']

            #order_info
            cart = Order.get_cart(request.user)
            items = cart.orderitem_set.all()
            if cart.amount == 0:
                return redirect('index')

            out = '' + str(first_name) + '  ' + str(last_name) + '\n'
            out += str(country) + '  ' + str(city) + '  ' + str(street) + '  ' + str(home_number) + '  ' + str(zip) + '\n'
            out += str(phone) + '\n' + '\n'
            out += str(cart) + '\n'
            for item in items:
                out += str(item) + ' size: ' + str(item.size) + ' price: ' + str(item.price) + ' quantity: ' + str(item.quantity) + '\n'
            out += '\n' + '\n' + '\n' + str(comment)

            msg = MIMEText(out, 'plain', 'utf-8')
            try:
                server = smtplib.SMTP("smtp.mail.ru", 2525)
                server.starttls()
                server.login(sender, password)

                server.sendmail(sender, my_recipient, msg.as_string())
                #server.sendmail(sender, shop_recipient, msg.as_string())
                #server.sendmail(sender, user_recipient, msg.as_string()) #copy for user, it can be diffrent messages for all 3 recipients
            except Exception as _ex:
                return HttpResponse(f"{_ex}\nCheck your login or password!")
            # try/except можно и без них по идее
            cart.make_order()
            return redirect('index')
    else:
        return HttpResponse('Error in form')

    return render(request, "shop/checkout.html", context=context)

# don't use
def success_view(request):
    return HttpResponse('Done!')

