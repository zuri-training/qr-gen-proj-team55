from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

# Create your models here.

# For business card
class qrcode_business(models.Model):
    company = models.CharField(max_length=200)
    about = models.TextField()
    opening_hours = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    logo = models.ImageField(upload_to="images")
    url = models.URLField(max_length=200)
    qr_code = models.ImageField(upload_to="qr_codes", blank=True)

    def __str__(self):
        return str(self.company)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.url)
        canvas = Image.new("RGB", (qrcode_img.size), "white")
        canvas.paste(qrcode_img)
        fname = f"qr_code-{self.id}-{self.name}.png"
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


# For App Download
class qrcode_appDownload(models.Model):
    app_name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to="images")
    url = models.URLField(max_length=200)
    qr_code = models.ImageField(upload_to="qr_codes", blank=True)

    def __str__(self):
        return str(self.app_name)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.url)
        canvas = Image.new("RGB", (qrcode_img.size), "white")
        canvas.paste(qrcode_img)
        fname = f"qr_code-{self.id}-{self.name}.png"
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


# Event
class qrcode_event(models.Model):
    organizer = models.CharField(max_length=200)
    about = models.TextField()
    event_name = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    organizer_email = models.EmailField(max_length=254)
    organizer_phone = models.CharField(max_length=12)
    logo = models.ImageField(upload_to="images")
    qr_code = models.ImageField(upload_to="qr_codes", blank=True)

    def __str__(self):
        return str(self.event_name)

    def save(self, *args, **kwargs):
        txt = f"{self.organizer}\n{self.about}\n{self.event_name}\n{self.venue}\n{self.organizer_email}\n{self.organizer_phone}\n{self.logo}"
        qrcode_img = qrcode.make(txt)
        canvas = Image.new("RGB", (qrcode_img.size), "white")
        canvas.paste(qrcode_img)
        fname = f"qr_code-{self.id}-{self.name}.png"
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
