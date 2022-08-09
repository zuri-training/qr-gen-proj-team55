from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
from authentication.models import CustomUser
# Create your models here.


class BaseModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_add_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    qr_code = models.ImageField(upload_to="qr_codes", blank=True)


    class Meta:
        abstract = True
    # def __str__(self):
    # return str(self.company)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new("RGB", (290, 290), "white")
        canvas.paste(qrcode_img)
        fname = f"qr_code-{self.id}-{self.name}.png"
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)



#For business card
class QrcodeBusiness(BaseModel):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    about = models.TextField ()
    opening_hours = models.CharField (max_length=200)
    address = models.CharField (max_length=200)
    email = models.EmailField (max_length=254)
    phone = models.CharField(max_length=12)
    # logo = models.ImageField (upload_to='images')
    # url = models.URLField(max_length=200)
    # qr_code = models.ImageField(upload_to="qr_codes", blank=True)

    def __str__(self):
        return str(self.company)

    # def save(self, *args, **kwargs):
    #     qrcode_img = qrcode.make(self.url)
    #     canvas = Image.new("RGB", (qrcode_img.size), "white")
    #     canvas.paste(qrcode_img)
    #     fname = f"qr_code-{self.id}-{self.name}.png"
    #     buffer = BytesIO()
    #     canvas.save(buffer, "PNG")
    #     self.qr_code.save(fname, File(buffer), save=False)
    #     canvas.close()
    #     super().save(*args, **kwargs)

#For App Download
class QrcodeAppDownload(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=200)
    description = models.TextField ()
    # logo = models.ImageField (upload_to='images')
    # url = models.URLField(max_length=200)
    # qr_code = models.ImageField(upload_to="qr_codes", blank=True)

    def __str__(self):
        return str(self.app_name)

    # def save(self, *args, **kwargs):
    #     qrcode_img = qrcode.make(self.url)
    #     canvas = Image.new("RGB", (qrcode_img.size), "white")
    #     canvas.paste(qrcode_img)
    #     fname = f"qr_code-{self.id}-{self.name}.png"
    #     buffer = BytesIO()
    #     canvas.save(buffer, "PNG")
    #     self.qr_code.save(fname, File(buffer), save=False)
    #     canvas.close()
    #     super().save(*args, **kwargs)

#Event
class QrcodeEvent(BaseModel):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    organizer = models.CharField(max_length=200)
    about = models.TextField ()
    event_name = models.CharField(max_length=200)
    venue = models.CharField (max_length=200)
    organizer_email = models.EmailField (max_length=254)
    organizer_phone = models.CharField(max_length=12)
    # logo = models.ImageField (upload_to='images')
    # qr_code = models.ImageField(upload_to="qr_codes", blank=True)

    def __str__(self):
        return str(self.event_name)

    # def save(self, *args, **kwargs):
    #     txt = f'{self.organizer}\n{self.about}\n{self.event_name}\n{self.venue}\n{self.organizer_email}\n{self.organizer_phone}\n{self.logo}'
    #     qrcode_img = qrcode.make(txt)
    #     canvas = Image.new("RGB", (qrcode_img.size), "white")
    #     canvas.paste(qrcode_img)
    #     fname = f"qr_code-{self.id}-{self.name}.png"
    #     buffer = BytesIO()
    #     canvas.save(buffer, "PNG")
    #     self.qr_code.save(fname, File(buffer), save=False)
    #     canvas.close()
    #     super().save(*args, **kwargs)