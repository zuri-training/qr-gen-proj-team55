from django.urls import path
from . import views

app_name = "authentication"
urlpatterns = [
    path("signup/", views.SignUp, name="signup"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path("", views.HomePage.as_view(), name="home"),
    path("profile/", views.ProfileUpdate, name="profile"),
]
