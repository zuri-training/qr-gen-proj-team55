# from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import MyUserManager

"""
- this model will allow user to have access_token and email will be a require field
- use the email and password instead of username and password
"""


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, max_length=120, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True)
    phone_Number = models.CharField(max_length=120, null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    website_url = models.URLField(null=True)
    url = models.URLField(null=True)
    bio = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
