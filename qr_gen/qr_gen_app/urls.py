from django.urls import path, include
from . import views

app_name = 'qr_gen_app'

urlpatterns = [
    path("",views.landing_page, name='home'),
    path("dashboard/",views.qr_dashboardview.as_view(), name='qr_dashboard'),
    path("dashboard3/",views.qr_dashboard3view, name='qr_dashboard3'),
]