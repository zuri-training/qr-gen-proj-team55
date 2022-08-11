from django.contrib import admin
from .models import QrcodeAppDownload, QrcodeBusiness, QrcodeEvent

# Register your models here.

admin.site.register(QrcodeEvent)
admin.site.register(QrcodeBusiness)
admin.site.register(QrcodeAppDownload)
