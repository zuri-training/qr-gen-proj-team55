from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)
from django.utils.translation import gettext_lazy as _  # python internationalization
from django.utils import timezone
from django.template.defaultfilters import slugify
from datetime import datetime, timedelta
from django.conf import settings
from . import utils


"""
- this model will allow user to have access_token and email will be a require field
- use the email and password instead of username and password
"""

# Create your models here.
class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        create and save a user with the given username, email and password
        """
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser must have is_superuser=True")

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(_("first_name"), max_length=120)
    last_name = models.CharField(_("last_name"), max_length=120)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    is_staff = models.BooleanField(_("active"), default=True)
    objects = MyUserManager()  # specify how object are retreive or deleted like CRUD
    email_verified = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "designated whether this users email is verified",
        ),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # this makes the not regenerate object
        ordering = "-created_at"  # object to be in descending

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    # create a default slug or user for users if blank

    def gen_random_slug(self):
        random_slug = slugify(
            self.first_name + self.last_name + utils.generate_random_id()
        )
        while CustomUser.objects.filter(slug=random_slug).exists():
            random_slug = slugify(
                self.first_name + self.last_name + utils.generate_random_id()
            )

        return random_slug

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = self.gen_random_slug()
        super().save(*args, **kwargs)
