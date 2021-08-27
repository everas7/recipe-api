from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test Creating a new user with an email is successfull"""
        email = 'test@dev.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email = email,
            password =  password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalized(self):
        """Test Creating a new user normalizes email"""
        email = 'test@DEV.COM'
        user = get_user_model().objects.create_user(email, 'somepassword')

        self.assertEqual(user.email, email.lower())