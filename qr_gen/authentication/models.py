from tkinter import CASCADE
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
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = MyUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    email = models.ForeignKey(CustomUser, max_length=120, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True)
    phone_Number = models.CharField(max_length=120, null=True)
    avater = models.ImageField(null=True, default="avatar.svg")
    bio = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "-updated",
        ]

    def __str__(self):
        return self.email
