import smtplib
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView
from django.shortcuts import redirect, render
from shop.forms import AddQuantityForm, CheckoutForm
from shop.models import Product, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
#хуита
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
import smtplib



def checkout(request):
    return render(request, "shop/checkout.html")

def cart(request):
    return render(request, "shop/cart.html")

def wishlist(request):
    return render(request, "shop/wishlist.html")

"""
def shop(request):
    products = Product.objects.all()
    return render(request, 'shop/shop.html', {'object_list': products})
"""

class ProductsListView(ListView):
    model = Product
    template_name = 'shop/shop.html'

class ProductsDetailView(DetailView):
    model = Product
    template_name = 'shop/product_details.html'


#def get_object_or_404(Product, pk):
 #   pass


@login_required(login_url=reverse_lazy('authentication/login'))
def add_item_to_cart(request, pk):
    if request.method == 'POST':
        quantity_form = AddQuantityForm(request.POST)
        if quantity_form.is_valid():
            quantity = quantity_form.cleaned_data['quantity']
            if quantity:
                cart = Order.get_cart(request.user)
                #product = Product.objects.get(pk=pk)
                product = get_object_or_404(Product, pk=pk)
                cart.orderitem_set.create(product=product,
                                          quantity=quantity,
                                          price=product.price)
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

    }
    return render(request, 'shop/cart.html', context)


@method_decorator(login_required, name='dispatch')
class CartDeleteItem(DeleteView):
    model = OrderItem
    template_name = 'shop/cart.html'
    success_url = reverse_lazy('shop/cart')

    # ѕроверка доступа
    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(order__user=self.request.user)
        return qs


@login_required(login_url=reverse_lazy('login'))
def make_order(request):
    cart = Order.get_cart(request.user)
    cart.make_order()
    return redirect('shop/shop')


def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = CheckoutForm()
    elif request.method == 'POST':
        #settings
        form = CheckoutForm(request.POST)
        sender = 'mr.olegron@mail.ru' #static
        password = "y8nEPsm64q6JVUTwT1gW" #static
        recipient = 'mr.olegron@mail.ru' #static, need 2 more recipients (to_email)
        recipient2 = 'demon.am@bk.ru'
        server = smtplib.SMTP("smtp.mail.ru", 2525)
        server.starttls()

        # если метод POST, проверим форму и отправим письмо
        if form.is_valid():
            #user_information
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            country = form.cleaned_data['country']
            street = form.cleaned_data['street']
            home_number = form.cleaned_data['home_number']
            city = form.cleaned_data['city']
            zip = form.cleaned_data['zip']
            phone = form.cleaned_data['phone']

            #order_info
            cart = Order.get_cart(request.user)
            items = cart.orderitem_set.all()

            out = '' + str(first_name) + '  ' + str(last_name) + '\n'
            out += str(country) + '  ' + str(city) + '  ' + str(street) + '  ' + str(home_number) + '  ' + str(zip) + '\n'
            out += str(phone) + '\n' + '\n'
            out += str(cart)
            for item in items:
                out += str(item) + '  ' + str(item.price) + '  ' + str(item.quantity) + '\n'
                # добавить размер еще, сначал просто в модель товара и сюда уже
            #sending email по идее не надо ничего провер€ть, просто отправл€ть, даннные всегда одни
            try:
                server.login(sender, password)
                server.sendmail(sender, recipient, out)
            except Exception as _ex:
                return HttpResponse(f"{_ex}\nCheck your login or password!")
            return redirect('shop/success')
    else:
        return HttpResponse('Error in form')

    return render(request, "shop/check.html", {'form': form})


def success_view(request):
    return HttpResponse('Done!')

