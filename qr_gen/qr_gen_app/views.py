from django.shortcuts import render
from django.views.generic import TemplateView
from .models import QrcodeBusiness, QrcodeAppDownload, QrcodeEvent
from authentication.models import CustomUser




class qr_dashboardview(TemplateView):
    template_name = "qr_gen_app/maindashboard.html"


class appdownload(TemplateView):
    template_name = 'qr_gen_app/sdashboard.html'


def QrcodeBusiness_view(request):
    name = "Here is your QR code"

    obj = QrcodeBusiness.objects.get(fk=CustomUser)

    context = {
        'name': name,
        'obj' : obj,
    }
    return render(request, 'qr_gen_app/QrcodeBusiness_view.html', context)

def save_QrcodeAppDownload(request):
    if request.method == "POST":
        name = request.POST.get("name")
        link = request.POST.get("link")
        company = request.POST.get("company")
        about = request.POST.get("about")
        hours = request.POST.get("hours")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        QrcodeBusiness = QrcodeBusiness(QRcode=name,url=link,company=company, about=about, opening_hours=hours,address=address,email=email,phone=phone)
        QrcodeBusiness.save()
    return render (request, "QrcodeBusiness_view.html")

