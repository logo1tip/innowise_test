from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from user.models import CustomUser


class AccountTests(APITestCase):

    def test_create_account(self):
      
        url = reverse('users')
        data = {
            "username": "DabApps",
            "first_name": "Dab",
            "last_name": "Apps",
            "email": "dabapps@mail.com",
            "role": "US"
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

