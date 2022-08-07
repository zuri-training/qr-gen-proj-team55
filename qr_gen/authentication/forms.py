from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm
from .models import CustomUser, Dashboard7


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["name", "email", "password1", "password2"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["email", "password"]


class UserForm(ModelForm):
    class Meta:
        model = Dashboard7
        fields = ["avater", "name", "email", "phone_Number", "bio"]
