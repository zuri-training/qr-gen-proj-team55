from django.urls import path, include
from . import views

app_name = "qr_gen_app"

urlpatterns = [
    path('qr_dashboard/', views.qr_dashboardview.as_view(), name='qr_dashboard'),
    path('appdownload/', views.appdownload.as_view(), name='appdownload'),
    path('QRcode/', views.QrcodeBusiness_view, name='businesscode'),
     
]
