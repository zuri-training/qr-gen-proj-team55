from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.SignUp, name="signup"),
    path("user-update/", views.updateUser7, name="user-update"),
]
