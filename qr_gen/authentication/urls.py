from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.SignUp, name="signup"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.log_out, name="logout"),
    path("profile/", views.updateUser7, name="profile"),
]
