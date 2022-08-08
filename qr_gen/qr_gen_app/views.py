from django.shortcuts import render

def landing_page(request):
    return render(request, "qr_code_app/LandingPage.html")

