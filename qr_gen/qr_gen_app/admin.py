from django.contrib import admin
from .models import QrcodeAppDownload, QrcodeBusiness, QrcodeEvent

# Register your models here.

admin.site.register(QrcodeAppDownload)
admin.site.register(QrcodeBusiness)
admin.site.register(QrcodeEvent)


