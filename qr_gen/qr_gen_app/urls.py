from django.urls import path, include
from . import views


app_name = 'qr_gen_app'

urlpatterns = [
    path("qr_dashboard/",views.qr_dashboardview.as_view(), name='qr_dashboard'),
    path("",views.QrcodeBusinessView, name='qr_dashboard3'),
    path('appdownload/', views.QrcodeAppDownloadView, name='appdownload'),
    path('event/', views.QrcodeEventView, name='event'),
]

