from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
from authentication.models import CustomUser

# Create your models here.


class BaseModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Qrcode_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    qr_code = models.ImageField(upload_to="qr_codes", blank=True)

    class Meta:
        abstract = True
   
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new("RGB", qrcode_img.size, "white")
        canvas.paste(qrcode_img)
        fname = f"qr_code-{self.id}-{self.name}.png"
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

# For business card
class QrcodeBusiness(BaseModel):
    company = models.CharField(max_length=200)
    about = models.TextField()
    opening_hours = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=12, null=True)
    url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return str(self.company)


# For App Download
class QrcodeAppDownload(BaseModel):
    app_name = models.CharField(max_length=200)
    description = models.TextField()
    androidApp_link = models.URLField(max_length=200, null=True)
    iosApp_link = models.URLField(max_length=200, null=True)
        
    def __str__(self):
        return str(self.app_name)
    

# Event
class QrcodeEvent(BaseModel):
    organizer = models.CharField(max_length=200)
    about = models.TextField()
    event_name = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    organizer_email = models.EmailField(max_length=254)
    organizer_phone = models.CharField(max_length=12)

    def __str__(self):
        return str(self.event_name)       