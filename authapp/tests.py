from django.test import TestCase
from authapp.models import User
from django.core.management import call_command
from django.test.client import Client
# Create your tests here.

class TestUserManagement(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')

        self.client = Client()

        self.superuser = User.objects.create_superuser('kostya', 'kostya@mail.ru', 'q1w1e1r1!')

        self.user = User.objects.create_user('geek', 'kostya27@mail.ru', 'w2e2r2t2!')

        self.user_with_name = User.objects.create_user('julia', 'julia@mail.ru', 'e1r1t2y4u5!', first_name='Julia')

    def test_user_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertEqual(response.context['title'], 'GeekShop')
        self.assertNotContains(response, 'Пользователь', status_code=200)

        self.client.login(username='kostya27',password='w2e2r2t2')

        response = self.client.get('/auth/login/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)

        response = self.client.get('/')
        self.assertContains(response, 'Пользователь', status_code=200)
        self.assertEqual(response.context['user'], self.user)

    def tearDown(self):
        call_command('sqlsequencerest', 'mainapp', 'autapp', 'ordersapp', 'basketapp')