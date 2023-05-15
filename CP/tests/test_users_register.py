from Core.models import User
from django.core import mail
from django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.email = 'testuser@example.com'
        self.password = 'testpassword'
        self.first_name = 'Tester'
        self.last_name = 'User'
        self.phone = 1234567890
        self.avatar = 'path/to/avatar.jpg'
    
    def test_registration_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_create_superuser(self):
        # Проверяем создание суперпользователя
        user = User.objects.create_superuser(
            username=self.username,
            email=self.email,
            password=self.password,
        )
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)