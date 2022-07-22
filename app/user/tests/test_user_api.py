from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""
    
    def test_create_valid_user(self):
        """Test create a user"""
        payload = {
            'email': 'testuser@gmail.com',
            'password': 'testuser123',
            'name': 'Test name'
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertEqual(user.email, payload['email'])
        self.assertEqual(user.name, payload['name'])
        self.assertNotIn('password', res.data)


    def test_user_exists(self):
        """Test creating user that already exists"""
        payload = {
            'email': 'testuser',
            'password': 'testuser123'
        }

        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_password_too_short(self):
        """Test that the password is too short"""
        payload = {'email': 'testuser@gmail.com', 'password': '123'}

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_exist = get_user_model().objects.filter(
            email = payload['email']
        ).exists()
        self.assertFalse(user_exist)


