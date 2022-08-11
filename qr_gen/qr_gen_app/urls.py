from django.urls import path, include
from . import views

<<<<<<< HEAD
app_name = 'qr_gen_app'

urlpatterns = [
    path("qr_dashboard/",views.qr_dashboardview.as_view(), name='qr_dashboard'),
    path("dashboard3/",views.qr_dashboard3view, name='qr_dashboard3'),
     path('appdownload/', views.appdownload.as_view(), name='appdownload'),
=======
app_name = "qr_gen_app"

urlpatterns = [
    path("qr_dashboard/", views.qr_dashboardview.as_view(), name="qr_dashboard"),
    path("appdownload/", views.appdownload.as_view(), name="appdownload"),
>>>>>>> 0c6b9a11a7c1777a542f9432996f86b8c546dae8
]
