from django.urls import path, include
from . import views


app_name = 'qr_gen_app'

urlpatterns = [
    path("",views.landing_page, name='home')
]