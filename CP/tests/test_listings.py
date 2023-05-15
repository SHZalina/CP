from rest_framework.test import APITestCase
from django.urls import reverse
from listings.models import Listing
from Core.models import User

class ApiTestCase(APITestCase):
    def test_get_status_code_listings(self) -> None:
        url = reverse('listings')
        response = self.client.get(url)
        self.assertEquals(200, response.status_code)

    def test_get_status_code_search(self) -> None:
        url = reverse('search')
        response = self.client.get(url)
        self.assertEquals(200, response.status_code)
    
    def test_get_status_code_create(self) -> None:
        url = reverse('create')
        response = self.client.get(url)
        self.assertEquals(302, response.status_code)
    
    '''
    def test_get_status_code_update(self) -> None:
        user = User.objects.create_user('tester_2', 'bread133@test.ru', 'test')
        listing_1 = Listing.objects.create(
            owner = user,
            title = 'Пес',
            category = 'Собака',
            breed = 'Дворняжка',
            address = 'Ленина 45',
            city = 'Казань',
            description = 'Пес',
            price = 100,
            photo_main = '/CP/static/img/Masha_1.jpg'
        )

        url = reverse('update', listing_1.data)
        print(url)
        # response = self.client.get(url)
        # self.assertEquals(200, response.status_code)

    '''