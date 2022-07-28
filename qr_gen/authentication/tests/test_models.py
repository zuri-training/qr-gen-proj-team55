from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    def test_creates_user(self):
        user = User.objects.create_user("awal", "awal@yahoo.com", "password133")
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, "awal@yahoo.com")

    def test_raises_error_no_username_is_supplied(self):
        self.assertRaises(
            ValueError,
            User.objects.create_user,
            username="",
            email="awal@yahoo.com",
            password="password133",
        )

    def test_raises_error_when_message_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, "The given username must be set"):
            User.objects.create_user(
                username="", email="awal@yahoo.com", password="password133"
            )

    def test_raises_error_no_email_is_supplied(self):
        self.assertRaises(
            ValueError,
            User.objects.create_user,
            username="awal",
            email="",
            password="password133",
        )

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, "The given email must be set"):
            User.objects.create_user(username="awal", email="", password="password133")

    def test_cant_creates_super_user_with_no_super_user_status(self):
        with self.assertRaisesMessage(
            ValueError, "superuser must have is_superuser=True"
        ):
            User.objects.create_superuser(
                username="awal",
                email="awal@yahoo.com",
                password="password133",
                is_staff=False,
            )

    def test_cant_creates_super_user_with_no_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, "superuser must have is_staff=True"):
            User.objects.create_superuser(
                username="awal",
                email="awal@yahoo.com",
                password="password133",
                is_superuser=False,
            )

    def test_creates_super_user(self):
        user = User.objects.create_user("awal", "awal@yahoo.com", "password133")
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, "awal@yahoo.com")
