from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm
from .models import Profile


class UserForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["avater", "name", "email", "phone_Number", "bio"]
