from django.shortcuts import render
from django.views.generic import TemplateView

class qr_dashboardview(TemplateView):
    template_name = 'qr_gen_app/maindashboard.html'

class appdownload(TemplateView):
    template_name = 'qr_gen_app/sdashboard.html'
