from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import QrcodeBusiness, QrcodeAppDownload, QrcodeEvent
from authentication.models import CustomUser




class qr_dashboardview(TemplateView):
    template_name = "qr_gen_app/maindashboard.html"


class appdownload(TemplateView):
    template_name = 'qr_gen_app/sdashboard.html'


def Qrcode_view(request):
    name = "Here is your QR code"

    obj = QrcodeBusiness.objects.get(fk=CustomUser)

    context = {
        'name': name,
        'obj' : obj,
    }
    return render(request, 'qr_gen_app/Qrcode_view.html', context)

def save_QrcodeAppDownload(request):
    if request.method == "POST":
        Aname = request.POST.get("APPname")
        description = request.POST.get("desc")
        url = request.POST.get("url")
        Qname = request.POST.get("QRcode")
        Inst_1 = QrcodeAppDownload(QRcode_name=Qname,url=url,app_name=Aname,description=description)
        Inst_1.save()
        return redirect ('/qrcode')
    return render (request, "qr_gen_app/sdashboard.html")

