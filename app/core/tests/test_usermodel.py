from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_save_model_user(self):
        email='theoreh"gmail.com'
        password='noworry'

        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_user_email_normalize(self):
        email='theoreh@GMAIL.COM'
        password='noworry'

        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email.lower())


    def test_user_email_validation(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'noworry')


    def test_save_model_super_user(self):
        email='theoreh@gmail.com'
        password='noworry'

        user=get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
