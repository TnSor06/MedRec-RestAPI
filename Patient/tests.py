from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CustomUser


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com', password='foo123bar', user_type=2)
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='', user_type=2)
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email='', password="foo123bar", user_type=2)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            'super@user.com', 'foo123bar', user_type=1)
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo123bar', user_type=1, is_superuser=False)
