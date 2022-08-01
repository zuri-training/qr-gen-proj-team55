from django.test import TestCase
from authentication.models import CustomUser


class CustomUserTestManager(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user("awal@yahoo.com", "password133")
        self.assertIsInstance(user, CustomUser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.email, "awal@yahoo.com")

    def test_raises_error_no_email_is_supplied(self):
        self.assertRaises(
            ValueError,
            CustomUser.objects.create_user,
            email="",
            password="password133",
        )

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, "The given email must be set"):
            CustomUser.objects.create_user(email="", password="password133")

    def test_cant_creates_super_user_with_no_super_user_status(self):
        with self.assertRaisesMessage(
            ValueError, "superuser must have is_superuser=True"
        ):
            CustomUser.objects.create_superuser(
                email="awal@yahoo.com",
                password="password133",
                is_staff=False,
            )

    def test_cant_creates_super_user_with_no_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, "superuser must have is_staff=True"):
            CustomUser.objects.create_superuser(
                email="awal@yahoo.com",
                password="password133",
                is_superuser=False,
            )

    def test_creates_super_user(self):
        user = CustomUser.objects.create_user("awal@yahoo.com", "password133")
        self.assertIsInstance(user, CustomUser)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, "awal@yahoo.com")
