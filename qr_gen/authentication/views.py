from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserForm
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
        return redirect("authentication:login")
    return render(request, "authentication/signup.html")


def Login(request):
    if request.user.is_authenticated:
        messages.info(
            request,
            mark_safe(f"You are already logged in as <b>{request.user.email}</b>."),
        )
        return redirect("authentication:home")

    username = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        # remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"{user.email} logged in successfully!")
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
    user = request.user
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user-profile", pk=user.id)

    return render(request, "authentication/profile.html", {"form": form})
