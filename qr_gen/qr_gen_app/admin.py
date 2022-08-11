from django.contrib import admin
from .models import qrcode_business, qrcode_appDownload, qrcode_event

# Register your models here.

admin.site.register(qrcode_business)
admin.site.register(qrcode_appDownload)
admin.site.register(qrcode_event)
