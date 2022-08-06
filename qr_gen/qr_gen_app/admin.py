from django.contrib import admin
from .models import qrcode_txt, qrcode_link

# Register your models here.

admin.site.register(qrcode_txt)
admin.site.register(qrcode_link)
