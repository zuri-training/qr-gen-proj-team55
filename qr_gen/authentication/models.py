from django.db import models
from helpers.models import TrackingModel
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings
import jwt

"""
- this model will allow user to have access_token and email will be arequire field

- use the email and password instead of username and password
"""

# Create your models here.
class MyUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        create and save a user with the given username, email and password
        """
        if not username:
            raise ValueError("The given username must be set")

        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser must have is_superuser=True")

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, TrackingModel):

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=50,
        unique=True,
        validators=[username_validator],
        error_messages={"unique": _("A user with this username already exit")},
    )
    first_name = models.CharField(_("first_name"), max_length=120)
    last_name = models.CharField(_("last_name"), max_length=120)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    date_joined = models.DateTimeField(_("date joined"), default=False)
    is_staff = models.BooleanField(_("active"), default=True)
    objects = MyUserManager()  # specify how object are retreive or deleted like CRUD
    email_verified = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "designated whether this users email is verified",
        ),
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    @property
    def token(self):
        token = jwt.encode(
            {
                "username": self.username,
                "email": self.email,
                "exp": datetime.utcnow() + timedelta(hours=24),
            },
            settings.SECRET_KEY,
            algorithm="HS256",
        )

        return token
