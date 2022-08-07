from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserForm


# Create your views here.
def SignUp(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            login(request, user)
            return redirect("home")
    else:
        messages.error(request, "An error occurred during registration")
    return render(request, "authentication/signup.html", {"form": form})


def loginPage(request):
    page = "login"
    User = CustomUser
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")

        try:
            user = User.object.object.get(email.email)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or password does not exit")
    context = {"page": page}
    return render(request, "authentication/login_register.html", context)


def log_out(request):
    logout(request)
    return redirect(reverse("authentication:login"))


@login_required(login_url="login")
def updateUser7(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user-profile", pk=user.id)
    return render(request, "authentication/profile.html", {"form": form})
