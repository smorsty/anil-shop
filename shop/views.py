from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView
from shop.forms import AddQuantityForm, CheckoutForm, PickSizeForm
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
    # если метод GET, вернем форму
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
        # по идее не нужно я же не буду со своей почты кидать ничего))
        sender = shop_sender
        password = shop_password
        my_recipient = 'diamond.coin@bk.ru'
        shop_recipient = 'anil_shop@mail.ru'
        user_recipient = request.user.email # get users email, for send him a mail with order_information

        # если метод POST, проверим форму и отправим письмо
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
                server.sendmail(sender, user_recipient, msg.as_string()) #copy for user, it can be diffrent messages for all 3 recipients
            except Exception as _ex:
                return HttpResponse(f"{_ex}\nCheck your login or password!")
            # try/except можно не проверять, все работает
            cart.make_order()
            return redirect('index')
    else:
        return HttpResponse('Error in form')

    return render(request, "shop/checkout.html", context=context)

# don't use
def success_view(request):
    return HttpResponse('Done!')

