from django.contrib import admin
from .models import QrcodeBusiness, QrcodeAppDownload, QrcodeEvent

# Register your models here.

admin.site.register(QrcodeBusiness)
admin.site.register(QrcodeAppDownload)
admin.site.register(QrcodeEvent)

