import zoneinfo
from decimal import Decimal
from unittest import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from shop.models import Product, Payment, OrderItem, Order


class TestDataBase(TestCase):
    fixtures = [
        "shop/fixtures/data.json"
    ]

    def setUp(self):
        self.user = User.objects.get(username='root')
        self.p = Product.objects.all().first()


    def test_user_exists(self):
        users = User.objects.all()
        users_number = users.count()
        user = users.first()
        self.assertEqual(users_number, 1)
        self.assertEqual(user.username, 'root')
        self.assertTrue(user.is_superuser)

    def test_user_check_password(self):
        self.assertTrue(self.user.check_password('root'))

    def test_all_data(self):
        self.assertGreater(Product.objects.all().count(), 0)
        self.assertGreater(Payment.objects.all().count(), 0)
        self.assertGreater(OrderItem.objects.all().count(), 0)
        self.assertGreater(Order.objects.all().count(), 0)

    def find_cart_number(self):
        cart_number = Order.objects.filter(user=self.user,
                                           status=Order.STATUS_CART
                                           ).count()
        return cart_number

    def test_function_get_cart(self):

        pass
        # 1 No Carts
        self.assertEqual(self.find_cart_number(), 0)# �����-�� �������� ������ ���� 0, � ���� 1 !!!!!
        # �� �� ���-�� ���������� ����� ������� test_cart_status_changing_after_applying_make_order?

        # 2 Create Cart
        Order.get_cart(self.user)
        self.assertEqual(self.find_cart_number(), 1)

        # 3 Get created cart
        Order.get_cart(self.user)
        self.assertEqual(self.find_cart_number(), 1)


    def test_cart_order_7_days(self):
        cart = Order.get_cart(self.user)
        cart.creation_time = timezone.datetime(2000, 1, 1, tzinfo=zoneinfo.ZoneInfo('UTC'))
        cart.save()
        cart = Order.get_cart(self.user)
        self.assertEqual((timezone.now() - cart.creation_time).days, 0)

    def test_recalculate_order_amount_after_changing_orderitem(self):

        # 1 Get order amount before changing
        cart = Order.get_cart(self.user)
        self.assertEqual(cart.amount, Decimal(0))

        # 2 -//- after adding item(s)
        i = OrderItem.objects.create(order=cart, product=self.p, price=2, quantity=2)
        i = OrderItem.objects.create(order=cart, product=self.p, price=2, quantity=3)
        cart = Order.get_cart(self.user)
        self.assertEqual(cart.amount, Decimal(10))

        # 3 -//- after deleting item(s)
        i.delete()
        cart = Order.get_cart(self.user)
        self.assertEqual(cart.amount, Decimal(4))

    def test_cart_status_changing_after_applying_make_order(self):

        # 1 Attempt to change the status for an empty cart
        cart = Order.get_cart(self.user)
        cart.make_order()
        self.assertEqual(cart.status, Order.STATUS_CART)

        # 2 Attempt to change the status for a non-empty cart
        i = OrderItem.objects.create(order=cart, product=self.p, price=2, quantity=3)
        cart.make_order()
        self.assertEqual(cart.status, Order.STATUS_WAITING_FOR_PAYMENT)

    def test_method_get_amount_of_unpaid_orders(self):

        # 1 Before creating cart
        amount = Order.get_amount_of_unpaid_orders(self.user)
        self.assertEqual(amount, Decimal(6))

        # 2 After creating cart
        cart = Order.get_cart(self.user)
        OrderItem.objects.create(order=cart, product=self.p, price=2, quantity=3)
        amount = Order.get_amount_of_unpaid_orders(self.user)
        self.assertEqual(amount, Decimal(6))

        # 3 After cart.make_order()
        cart.make_order()
        amount = Order.get_amount_of_unpaid_orders(self.user)
        self.assertEqual(amount, Decimal(12))

        # 4 After order is Paid
        cart.status = Order.STATUS_PAID
        cart.save()
        amount = Order.get_amount_of_unpaid_orders(self.user)
        self.assertEqual(amount, Decimal(6))

        # 5After delete all orders
        Order.objects.all().delete()
        amount = Order.get_amount_of_unpaid_orders(self.user)
        self.assertEqual(amount, Decimal(0))

    def test_method_get_balance(self):

        # 1 Before adding payment
        amount = Payment.get_balance(self.user)
        self.assertEqual(amount, Decimal(5))

        # 2 After adding payment
        Payment.objects.create(user=self.user, amount=100)
        amount = Payment.get_balance(self.user)
        self.assertEqual(amount, Decimal(105))

        # 3 After adding some payments
        Payment.objects.create(user=self.user, amount=-50)
        amount = Payment.get_balance(self.user)
        self.assertEqual(amount, Decimal(55))

        # 4 No payments
        Payment.objects.all().delete()
        amount = Payment.get_balance(self.user)
        self.assertEqual(amount, Decimal(0))

    def test_auto_payment_after_apply_make_order_true(self):
        Order.objects.all().delete()
        cart = Order.get_cart(self.user)
        OrderItem.objects.create(order=cart, product=self.p, price=2, quantity=2)
        self.assertEqual(Payment.get_balance(self.user), Decimal(5))
        cart.make_order()
        self.assertEqual(Payment.get_balance(self.user), Decimal(1))

    def test_auto_payment_after_apply_make_order_false(self):
        Order.objects.all().delete()
        cart = Order.get_cart(self.user)
        OrderItem.objects.create(order=cart, product=self.p, price=2, quantity=1000)
        cart.make_order()
        self.assertEqual(Payment.get_balance(self.user), Decimal(5))

    def test_auto_payment_after_add_required_payment(self):
        Payment.objects.create(user=self.user, amount=556)
        self.assertEqual(Payment.get_balance(self.user), Decimal(0))
        amount = Order.get_amount_of_unpaid_orders(self.user)
        self.assertEqual(amount, Decimal(0))

    def test_auto_payment_for_earlier_order(self):
        cart = Order.get_cart(self.user)
        OrderItem.objects.create(order=cart, product=self.p, price=2, quantity=500)
        Payment.objects.create(user=self.user, amount=1000)
        self.assertEqual(Payment.get_balance(self.user), Decimal(0))
        amount = Order.get_amount_of_unpaid_orders(self.user)
        self.assertEqual(amount, Decimal(1000))
