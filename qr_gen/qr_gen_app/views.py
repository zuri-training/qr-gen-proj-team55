

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView




# class qr_dashboardview(TemplateView):
#     template_name = 'qr_gen_app/maindashboard.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['qrcode_business'] = qrcode_business.objects.all()
    #     context['qrcode_appDownload'] = qrcode_appDownload.objects.all()
    #     context['qrcode_event'] = qrcode_event.objects.all()
    #     return context
    




@login_required
def qr_dashboard3view(request):
    
    if request.method =='POST':
        company= request.POST.get('company_name', None)
        about = request.POST.get('about', None)
        opening_hours = request.POST.get('opening_hours', None)
        contact_details = request.POST.get('contact_details', None)
        web_url = request.POST.get('web_url', None)

        return redirect ('dashborard3.html')

    return render(request, 'qr_gen_app/dashboard3.html')







from django.shortcuts import render
from django.views.generic import TemplateView


class qr_dashboardview(TemplateView):
    template_name = 'qr_gen_app/maindashboard.html'

class appdownload(TemplateView):
    template_name = 'qr_gen_app/sdashboard.html'
