from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models



def sample_user(email='testuser4@gmail.com', password='testuser4123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user successfully"""
        
        email = 'test@gmail.com'
        password = 'test123'

        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        # self.assertTrue(user.is_active)
        # self.assertFalse(user.is_staff)""

    def test_normalized_email(self):
        """Testing a normalized email"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    
    def test_user_with_invalid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_create_superuser(self):
        """Test creating a new super user"""
        email = 'superuser@gmail.com'
        password = 'superuser123'

        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


    
    
    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )


        self.assertEqual(str(tag), tag.name)

    
