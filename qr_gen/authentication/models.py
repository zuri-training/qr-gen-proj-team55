from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
)
from django.utils.translation import gettext_lazy as _  # python internationalization
from django.utils import timezone
from django.template.defaultfilters import slugify
from datetime import datetime, timedelta
from django.conf import settings
from . import utils
from .managers import MyUserManager


"""
- this model will allow user to have access_token and email will be a require field
- use the email and password instead of username and password
"""

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email


"""
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
"""
