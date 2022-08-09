
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from .models import qrcode_business, qrcode_appDownload, qrcode_event
from .models import QrUser

User = QrUser

@login_required
def Dashboard3View(request,pk):
    user = User.objects.get(pk=id)
    if request.method =='POST':
        company= request.POST.get('company_name', None)
        about = request.POST.get('about', None)
        opening_hours = request.POST.get('opening_hours', None)
        contact_details = request.POST.get('contact_details', None)
        web_url = request.POST.get('web_url', None)

        return redirect ('dashborard3.html', pk=user.id)

    return render(request, 'qr_gen_app/dashboard3.html')








def landing_page(request):
    return render(request, "qr_code_app/LandingPage.html")

