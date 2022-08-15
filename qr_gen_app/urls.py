from django.urls import path, include
from . import views


app_name = 'qr_gen_app'

urlpatterns = [
    path("qr_dashboard/",views.qr_dashboardview.as_view(), name='qr_dashboard'),
    path("qr_dashboard3/",views.QrcodeBusinessView, name='qr_dashboard3'),
    path("qr_dashboard4/",views.QrcodeAppDownloadView, name='qr_dashboard4'),
    path("qr_dashboard5/",views.QrcodeEventView, name='qr_dashboard5'),
    path("business_code/", views.business_qrcode_view, name='business_code'),
    path("app_code/", views.app_qrcode_view, name='app_code'),
    path("event_code/", views.event_qrcode_view, name='event_code'),

]
    
