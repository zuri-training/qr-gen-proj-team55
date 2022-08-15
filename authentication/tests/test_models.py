import django
from django.test import TestCase
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model


class CustomUserTestManager(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="awal@yahoo.com", password="foo")
        self.assertIsInstance(user, get_user_model())
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.email, "awal@yahoo.com")

    def test_raises_error_no_email_is_supplied(self):
        self.assertRaises(
            ValueError,
            get_user_model().objects.create_user,
            email="",
            password="foo",
        )

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        User = get_user_model()
        with self.assertRaisesMessage(ValueError, "The given email must be set"):
            User.objects.create_user(email="", password="foo")

    def test_cant_creates_super_user_with_no_super_user_status(self):
        User = get_user_model()
        with self.assertRaisesMessage(
            ValueError, "superuser must have is_superuser=True"
        ):
            User.objects.create_superuser(
                email="awal@yahoo.com",
                password="foo",
                is_staff=False,
            )

    def test_cant_creates_super_user_with_no_is_staff_status(self):
        User = get_user_model()
        with self.assertRaisesMessage(ValueError, "superuser must have is_staff=True"):
            User.objects.create_superuser(
                email="awal@yahoo.com",
                password="foo",
                is_superuser=False,
            )

    def test_creates_superuser(self):
        User = get_user_model()
        user = User.objects.create_user(email="awal@yahoo.com", password="foo")
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, "awal@yahoo.com")


class CustomUserModelTest(TestCase):
    def test_user_slug_is_unique(self):
        User = get_user_model()
        user = User.objects.create_user(email="awal@yahoo.com", password="foo")
        user2 = User.objects.create_user(email="awal@yahoo.com", password="foo")
        self.assertNotEqual(user.slug, user2.slug)

        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                email="user@email.com", slug="user-slug", password="foo"
            )
            User.objects.create_user(
                email="user2@email.com", slug="user-slug", password="foo"
            )

    def test__str__(self):
        User = get_user_model()
        user = User.objects.create_user(email="user@email.com", password="foo")
        self.assertEqual(str(user), user.email)

    def test_user_slug_is_generated_if_blank(self):
        User = get_user_model()
        user = User.objects.create_user(email="user@email.com", password="foo")
        self.assertNotEqual(user.slug, "")

    def test_user_slug_is_not_overwritten(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="user@email.com", password="foo", slug="weird-slug"
        )
        self.assertEqual(user.slug, "weird-slug")
