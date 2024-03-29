from decimal import Decimal

from django.db import models, transaction
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone




CATEGORY_CHOICE = (
    ('clothes', 'CLOTHES'),
    ('shoes', 'SHOES'),
    ('accessories', 'ACCESSORIES'),
)

PRODUCT_TYPE_CHOICE = (
    ('Clothes',
     (
        ('t-shirt', 'T-SHIRT'),
        ('shirt', 'SHIRT'),
        ('polo', 'POLO'),
        ('sweater', 'SWEATER'),
        ('hoodie', 'HOODIE'),
        ('turtleneck', 'TURTLENECK'),#���������
        ('Longs-Leeve', 'LONGSLEEVE'),

        ('shorts', 'SHORTS'),
        ('trousers', 'TROUSERS'),
        ('jeans', 'JEANS'),
        ('sport_trousers', 'SPORT_TROUSERS'),

        ('bomber', 'BOMBER'),
        ('jacket', 'JACKET'),
        ('vest', 'VEST'),#������
        ('coat', 'COAT'),
        ('park', 'PARK'),
        ('down jacket', 'DOWN JACKET'),#�������

        ('sport_costumes', 'SPORT_COSTUMES'),
     )
    ),
    ('Shoes',
     (
        ('sneakers', 'SNEAKERS'),
        ('boots', 'BOOTS'),
        ('flip_flops', 'FLIP_FLOPS'),
        ('sandals', 'SANDALS'),

     )
     ),
    ('Accessories',
     (
        ('accessories', 'ACCESSORIES'),
     )
     ),
    ('technique',
     (
         ('dyson', 'DYSON'),

     )
    ),
)

GENDER_CHOICE = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
)

BRAND_CHOICE = (
    ('Nike', 'NIKE'),
    ('Adidas', 'ADIDAS'),
    ('Hugo Boss', 'Hugo Boss'),
    ('Zara', 'Zara'),
    ('Tommy Hilfiger', 'Tommy Hilfiger'),
    ('Calvin Klein', 'Calvin Klein'),
    ('Tommy jeans', 'Tommy jeans'),
    ('Calvin Klein Jeans', 'Calvin Klein Jeans'),
    ('Marco di radi', 'Marco di radi'),
    ('Polo Assn', 'Polo Assn'),
    ('Reebok', 'Reebok'),
    ('Polo Ralph Lauren', 'Polo Ralph Lauren'),
    ('Marco polo', 'Marco polo'),
    ('New Balance', 'New Balance'),
    ('Timberland', 'Timberland'),
    ('Nike SB', 'Nike SB'),
    ('Adidas Original', 'Adidas Original'),
    ('Dyson', 'Dyson'),
    ('H&M', 'H&M'),
    ('Massimo Dutti', 'Massimo Dutti'),
    ('Cos', 'Cos'),
    ('Jordan', 'Jordan'),
    ('Levis', 'Levis'),
    ('Sporty&rich', 'Sporty&rich'),
    ('Mango', 'Mango'),
    ('UGG', 'UGG'),
    ('Oysho', 'Oysho'),
    ('Converse', 'Converse'),
    ('Puma', 'Puma'),
    ('Crocs', 'Crocs'),
    ('The North Face', 'The North Face'),
    ("Victoria Secret", "Victoria Secret"),
    ("The Other Stories", "The Other Stories"),
)


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='product_name', blank=True, null=True)
    code = models.CharField(max_length=255, verbose_name='product_code', blank=True, null=True)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICE, default='shoes', verbose_name='product_category')
    product_type = models.CharField(max_length=255, choices=PRODUCT_TYPE_CHOICE, default='sneakers', verbose_name='product_type')
    brand = models.CharField(max_length=255, choices=BRAND_CHOICE, default='Nike', verbose_name='product_brand')
    gender = models.CharField(max_length=25, choices=GENDER_CHOICE, default='male', verbose_name='product_gender')
    price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    old_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    # ���� ���� ����� �� ���� ���� � price, � ������ � old_price, ���� ��� ������ �� ��������� ���������� � ��� ����������
    image = models.ImageField(upload_to='shop/images', blank=True, null=True)
    image2 = models.ImageField(upload_to='shop/images', blank=True, null=True)
    image3 = models.ImageField(upload_to='shop/images', blank=True, null=True)
    image4 = models.ImageField(upload_to='shop/images', blank=True, null=True)
    image5 = models.ImageField(upload_to='shop/images', blank=True, null=True)
    note = models.TextField(blank=True, null=True)#comment


    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.name}' # ��� ��� self.price

    def discount(self):
        return int((((self.old_price - self.price) / self.price) * 100 ))


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.user} - {self.amount}'

    @staticmethod
    def get_balance(user: User):
        amount = Payment.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum']
        return amount or Decimal(0)


class Order(models.Model):
    STATUS_CART = 'cart'
    STATUS_WAITING_FOR_PAYMENT = 'waiting_for_payment'
    STATUS_PAID = 'paid'
    STATUS_CHOICES = [
        (STATUS_CART, 'cart'),
        (STATUS_WAITING_FOR_PAYMENT, 'waiting_for_payment'),
        (STATUS_PAID, 'paid')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # items = models.ManyToManyField(OrderItem, related_name='orders')
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=STATUS_CART)
    amount = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    delivery = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.user} - {self.total} - {self.status}'
    
    @property
    def total(self):
        return self.amount + self.delivery

    @staticmethod
    def get_cart(user: User):
        cart = Order.objects.filter(user=user,
                                    status=Order.STATUS_CART
                                    ).first()


        if cart and (timezone.now() - cart.creation_time).days > 7:
            cart.delete()
            cart = None

        if not cart:
            cart = Order.objects.create(user=user,
                                        status=Order.STATUS_CART,
                                        amount=0)

        return cart

    def get_amount(self):
        amount = Decimal(0)
        for item in self.orderitem_set.all():
            amount += item.amount
        if amount < 7000:
            self.delivery = 1000
        else:
            self.delivery = 0

        return amount

    def make_order(self):
        items = self.orderitem_set.all()
        if items and self.status == Order.STATUS_CART:
            self.status = Order.STATUS_WAITING_FOR_PAYMENT
            self.save()
            auto_payment_unpaid_orders(self.user)

    @staticmethod
    def get_amount_of_unpaid_orders(user: User):
        amount = Order.objects.filter(user=user,
                                      status=Order.STATUS_WAITING_FOR_PAYMENT
                                      ).aggregate(Sum('amount'))['amount__sum']
        return amount or Decimal(0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=0)
    #discount = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    size = models.CharField(max_length=10, default='')
    #clothes_size = models.CharField(max_length=255, choices=SIZE_CLOTHES_CHOICE, default='M',
     #                           verbose_name='clothes_size', blank=True, null=True)
    #shoes_size = models.CharField(max_length=255, choices=SIZE_SHOES_CHOICE, default='41',
     #                           verbose_name='shoes_size', blank=True, null=True)
    # ��� ������� �� �����, ������ � ��������, ����� ����� ����� ������� �������
    # size field with choise

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.product}' #��� ��� self.price

    @property
    def amount(self):
        return self.quantity * self.price



@transaction.atomic()
def auto_payment_unpaid_orders(user: User):
    unpaid_orders = Order.objects.filter(user=user,
                                         status=Order.STATUS_WAITING_FOR_PAYMENT)
    for order in unpaid_orders:
        if Payment.get_balance(user) < order.amount:
            break

        order.payment = Payment.objects.all().last()
        order.status = Order.STATUS_PAID
        order.save()
        Payment.objects.create(user=user,
                               amount=-order.amount)



@receiver(post_save, sender=OrderItem)
def recalculate_order_amount_after_save(sender, instance, **kwargs):
    order = instance.order
    order.amount = order.get_amount()
    order.save()


@receiver(post_delete, sender=OrderItem)
def recalculate_order_amount_after_delete(sender, instance, **kwargs):
    order = instance.order
    order.amount = order.get_amount()
    order.save()


@receiver(post_save, sender=Payment)
def auto_payment(sender, instance, **kwargs):
    user = instance.user
    auto_payment_unpaid_orders(user)
