from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
import qrcode.image.svg
# Create your models here.

class qrcode_txt(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.text)
        canvas = Image.new('RGB', (qrcode_img.size), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class qrcode_link(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.url)
        canvas = Image.new('RGB', (qrcode_img.size), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


        qrcode_img = qrcode.make(self.url, image_factory=qrcode.image.svg.SvgImage)
        fname = f'qr_code-{self.name}.svg'
        qrcode_img.save(fname)