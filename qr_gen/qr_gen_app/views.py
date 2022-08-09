from django.shortcuts import render
from .models import qrcode_link, qrcode_txt

def landing_page(request):
    return render(request, "qr_code_app/LandingPage.html")

