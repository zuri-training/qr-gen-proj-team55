from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm
from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["name", "email", "password1", "password2"]


class UserForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["avater", "name", "email", "phone_Number", "bio"]
