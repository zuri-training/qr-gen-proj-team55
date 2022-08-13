from django.urls import path, include
from . import views


app_name = "qr_gen_app"

urlpatterns = [
    path("qr_dashboard/", views.qr_dashboardview.as_view(), name="qr_dashboard"),
    path("", views.QrcodeBusinessView, name="qr_dashboard3"),
    path("qr_dashboard4/", views.QrcodeAppDownloadView, name="qr_dashboard4"),
    path("qr_dashboard5/", views.QrcodeEventView, name="qr_dashboard5"),
]
