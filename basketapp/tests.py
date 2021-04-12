from django.test import TestCase
from django.test.client import Client
from authapp.models import User
from django.core.management import call_command

# Create your tests here.
class TestBasketCreate(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

        self.user = User.objects.create_user('kostya02', 'kostya02@geekshop.local', 'konstantin')

    def test_basket_add(self):

        # пробуем добавить товар в коризну
        response = self.client.get('/baskets/basket_add/1/')
        # т.к. пользователь не авторизован, то нас перенаправляет на страницу авторизации
        self.assertEqual(response.url, '/auth/login/?next=/baskets/basket_add/1/')
        # если я правильно понял, то 302 код - перенаправление, потому при тесте ответа страницы используем его
        self.assertEqual(response.status_code, 302)

        # авторизовываемся
        self.client.login(username='kostya02', password='konstantin')

        # пробуем снова добавить товар в корзину и получаем ответ от страницы на перенаправление
        response = self.client.get('/baskets/basket_add/1/')
        self.assertEqual(response.status_code, 302)


    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basketapp')