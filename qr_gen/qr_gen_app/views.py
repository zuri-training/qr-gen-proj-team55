from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import QrcodeBusiness, QrcodeAppDownload, QrcodeEvent
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

# user = BaseModel
class qr_dashboardview(TemplateView):
    template_name = "qr_gen_app/maindashboard.html"

@login_required
def QrcodeBusinessView(request):
    
    if request.method =='POST':
        company= request.POST.get('company', None)
        about = request.POST.get('about', None)
        opening_hours = request.POST.get('opening_hours', None)
        address = request.POST.get('address', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phoneNo', None)
        url = request.POST.get('websiteURL', None)
        business = QrcodeBusiness(user=request.user,
        company=company, 
        about=about,
        opening_hours=opening_hours,
        address=address,
        email=email,
        phone=phone,
        url=url)
        business.save()
        
        messages.success(request, 'Business Card Created Successfully')
        return redirect ('qr_gen_app:qr_dashboard')
    return render(request, 'qr_gen_app/dashboard3.html')

    
@login_required
def QrcodeAppDownloadView(request):
    if request.method =='POST':
        app_name = request.POST.get('app_name', None)
        description = request.POST.get('description', None)
        androidApp_link = request.POST.get('androidApp_link', None)
        iosApp_link = request.POST.get('iosApp_link', None)
        appdownload = QrcodeAppDownload(user=request.user,
        app_name=app_name, 
        description=description,
        androidApp_link=androidApp_link,
        iosApp_link=iosApp_link)
        appdownload.save()
        
        messages.success(request, 'App Download Created Successfully')
        return redirect ('qr_gen_app:qr_dashboard')

    return render(request, 'qr_gen_app/dashboard4.html')


@login_required
def QrcodeEventView(request):
    if request.method =='POST':
        organizer = request.POST.get('organizer', None)
        about = request.POST.get('about', None)
        event_name = request.POST.get('event_name', None)
        venue = request.POST.get('venue', None)
        organizer_email = request.POST.get('organizer_email', None)
        organizer_phone = request.POST.get('organizer_phone', None)
        event = QrcodeEvent(user=request.user,
        organizer=organizer,
        about=about,
        event_name=event_name,
        venue=venue,
        organizer_email=organizer_email,
        organizer_phone=organizer_phone)
        event.save()
        messages.success(request, 'Event Created Successfully')
        return redirect ('qr_gen_app:qr_dashboard')

    return render(request, 'qr_gen_app/dashboard5.html')