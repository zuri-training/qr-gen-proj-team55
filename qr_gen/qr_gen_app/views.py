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

