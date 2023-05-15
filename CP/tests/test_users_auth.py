from Core.models import User
from django.test import TestCase
from django.urls import reverse


class LoginTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.email = 'test@test.com'
        self.user = User.objects.create_user(username=self.username, email = self.email, password=self.password)

    def test_login_view_302(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    # Проверяем успешный вход пользователя
    def test_valid_login(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertRedirects(response, reverse('index'))
        self.assertTrue('_auth_user_id' in self.client.session)  # Проверяем, что пользователь авторизован

    # Проверяем неудачный вход пользователя с неверными учетными данными
    def test_invalid_login(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 302)  # Проверяем, что вход отклонен
        self.assertFalse('_auth_user_id' in self.client.session)  # Проверяем, что пользователь не авторизован

    # Проверяем выход пользователя из аккаунта
    def test_logout(self):
        self.client.login(username=self.username, password=self.password)  # Авторизуем пользователя
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('index'))  # Проверяем перенаправление на главную страницу
        self.assertFalse('_auth_user_id' in self.client.session)  # Проверяем, что пользователь не авторизован