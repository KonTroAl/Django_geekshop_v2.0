from django.test import TestCase
from django.test.client import Client
from authapp.models import User
from mainapp.models import Product
from ordersapp.models import Order, OrderItem
from django.core.management import call_command


# Create your tests here.
class TestBasketCreate(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

        self.user = User.objects.create_user('kostya02', 'kostya02@geekshop.local', 'konstantin')
        product_1 = Product.objects.get(id=1)
        product_2 = Product.objects.get(id=2)

        order = Order.objects.create(user_id=1)
        # Цена за 5 товаров первого продукта: 30 450
        self.order_item_1 = OrderItem.objects.create(order=order,
                                                     product=product_1,
                                                     quantity=5)
        # Цена за 3 товаров второго продукта: 71 175
        self.order_item_2 = OrderItem.objects.create(order=order,
                                                     product=product_2,
                                                     quantity=3)

    def test_get_total_quantity(self):
        order = Order.objects.get(id=1)
        order_quantity = order.get_total_quantity()

        self.assertEqual(order_quantity, 8)

    def test_get_product_type_quantity(self):
        order = Order.objects.get(id=1)
        product_type_quantity = order.get_product_type_quantity()

        self.assertEqual(product_type_quantity, 2)

    def test_get_total_cost(self):
        order = Order.objects.get(id=1)
        total_coast = order.get_total_cost()

        self.assertEqual(total_coast, 101625)

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basketapp')
