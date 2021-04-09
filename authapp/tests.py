from django.test import TestCase
from django.test.client import Client
from authapp.models import User
from django.core.management import call_command


class TestUserManagement(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

        self.superuser = User.objects.create_superuser('Kostya', 'kostya@geekshop.local', 'konstantin')

        self.user = User.objects.create_user('kostya02', 'kostya02@geekshop.local', 'konstantin')

        self.user_with__first_name = User.objects.create_user('julia', 'julia@geekshop.local', 'juliatrosh', first_name='Julia')

    def test_user_login(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.context['user'].is_anonymous)

        self.assertEqual(response.context['title'], 'GeekShop')
        self.assertNotContains(response, 'Пользователь', status_code=200)

        self.client.login(username='kostya02', password='konstantin')

        response = self.client.get('/auth/login/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)

        response = self.client.get('/')
        self.assertEqual(response.context['user'], self.user)

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basketapp')