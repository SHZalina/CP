from Core.models import User
from django.core import mail
from django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def test_registration_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)