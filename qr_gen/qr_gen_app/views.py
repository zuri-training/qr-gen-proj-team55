from django.shortcuts import render

def landing_page(request):
    return render(request, "qr_code_app/LandingPage.html")

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