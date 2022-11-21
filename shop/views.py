from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from shop.forms import AddQuantityForm
from shop.models import Product, Order
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def checkout(request):
    return render(request, "shop/checkout.html")

def wishlist(request):
    return render(request, "shop/wishlist.html")

class ProductsListView(ListView):
    model = Product
    template_name = 'shop/shop.html'

class ProductsDetailView(DetailView):
    model = Product
    template_name = 'shop/product_details.html'


def get_object_or_404(Product, pk):
    pass


@login_required(login_url=reverse_lazy('authentication/login'))
def add_item_to_cart(request, pk):
    if request.method == 'POST':
        quantity_form = AddQuantityForm(request.POST)
        if quantity_form.is_valid():
            quantity = quantity_form.cleaned_data['quantity']
            if quantity:
                cart = Order.get_cart(request.user)
                product = Product.objects.get(pk=pk)
                #product = get_object_or_404(Product, pk=pk)
                cart.orderitem_set.create(product=product,
                                          quantity=quantity,
                                          price=product.price)
                cart.save()
                return redirect('shop/cart')
        else:
            pass
    return redirect('shop/shop')


@login_required(login_url=reverse_lazy('login'))
def cart_view(request):
    cart = Order.get_cart(request.user)
    items = cart.orderitem_set.all()
    context = {
        'cart': cart,
        'items': items,
    }
    return render(request, 'shop/cart.html', context)

