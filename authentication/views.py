from re import template
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from .models import Profile

# from .forms import UserForm
from django.views.generic import TemplateView

User = CustomUser
# Create your views here.
def SignUp(request):
    template_name = "authentication/registration.html"
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cnfrm_password = request.POST.get("cnfrm_password")
        if password != cnfrm_password:
            messages.warning(request, "Passwords do not match!")

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already exists")
            return redirect("authentication:signup")

        user = User.objects.create_user(email=email, password=password)
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect("authentication:profile")
    return render(request, template_name)


def Login(request):
    if request.user.is_authenticated:
        messages.info(
            request,
            mark_safe(f"You are already logged in as <b>{request.user.email}</b>."),
        )
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            messages.success(request, f"{user.email} logged in successfully!")
            return redirect("qr_gen_app:qr_dashboard")
        else:
            messages.warning(request, "Please check your credentials")
      return render(request, "authentication/login.html")


def Logout(request):
    if request.method == "POST":
        messages.INFO(request, "You have logged out successfully!")
        logout(request)
    return redirect("authentication:home")



class HomePage(TemplateView):
    template_name = "authentication/index.html"


@login_required(login_url="login")
def ProfileUpdate(request):
    template_name = "authentication/dashboard-signup.html"
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_Number = request.POST.get("phoneNo")
        #we'll modify the avater later
        avatar = request.FILES.get("avatar")
        bio = request.POST.get("bio")
        url = request.POST.get("url")
        website_url = request.POST.get("website-url")

        profile = Profile.objects.create(user=request.user,
        name=name, 
        phone_Number=phone_Number,
        avatar=avatar,
        bio=bio, 
        url=url,
        website_url=website_url)
        profile.save()
        #messages.success(request, "Welcome,You can now Generate QR ")
        return redirect("qr_gen_app:qr_dashboard")

    return render(request, template_name)
