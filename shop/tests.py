from unittest import TestCase
from django.contrib.auth.models import User

from shop.models import Product, Payment, OrderItem, Order


class TestDataBase(TestCase):
    fixtures = [
        "shop/fixtures/data.json"
    ]

    def setUp(self):
        self.user = User.objects.get(username='root')


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
        