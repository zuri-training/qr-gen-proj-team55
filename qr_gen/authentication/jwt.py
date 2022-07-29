from rest_framework.authentication import get_authorization_header, BaseAuthentication
from authentication.models import User
from rest_framework import exceptions
import jwt

from django.conf import settings


class JWTAthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request)

        auth_data = auth_header.decode("utf-8")
        auth_token = auth_data.split(" ")

        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed("Taken not valid")
        token = auth_token[1]
        try:

            payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            username = payload["username"]
            user = User.objects.get(username=username)
            return (user, token)

        except jwt.ExpiredSignatiureError as ex:
            raise exceptions.AuthenticationFailed("Token is expired login again")

        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed("Token is invalid")

        except User.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed("No such user")

        return super().authenticate(request)
