from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages

# from .forms import UserForm
from django.views.generic import TemplateView

User = CustomUser
# Create your views here.
def SignUp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        cnfrm_password = request.POST.get("cnfrm_password")
        # print(email)
        # print(password)

        if password != cnfrm_password:
            messages.error(request, "Passwords do not match!")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("authentication:signup")

        user = User.objects.create(email=email)
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect("authentication:home")
    return render(request, "authentication/signup.html")


def Login(request):
    if request.user.is_authenticated:
        messages.info(
            request,
            mark_safe(f"You are already logged in as <b>{request.user.email}</b>."),
        )
        return redirect("qr_gen_app:qr_dashboard")

    username = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email)
        print(password)
        # remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            messages.success(request, f"{user.email} logged in successfully!")
            return redirect("qr_gen_app:qr_dashboard")

            # if not remember_me:
            #     request.session.set_expiry(0)
            # return redirect('website:index')
        else:
            messages.warning(request, "Please check your credentials")

    return render(request, "authentication/login.html")


def Logout(request):
    logout(request)
    messages.success(request, "You have logged out successfully!")
    return redirect("authentication:home")


class HomePage(TemplateView):
    template_name = "authentication/home.html"


@login_required(login_url="login")
def ProfileUpdate(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        number = request.POST.get("number")
        user = User.save()
        messages.success(request, "Welcome,You can now Generate QR ")
    return render(request, "qr_gen_app/profile.html")
