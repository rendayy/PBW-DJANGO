from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os

class Create(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    STATUS_CHOICES = (
        ('p', 'Pending'),
        ('a', 'Approved'),
        ('r', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gambar = models.ImageField(upload_to='uploads/')  # gambar asli
    thumbnail = models.ImageField(upload_to='uploads/thumbnails/', blank=True, null=True)  # thumbnail
    kategori = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    judul = models.CharField(max_length=200)
    tanggal_upload = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.gambar and not self.thumbnail:
            img = Image.open(self.gambar)
            img = img.convert('RGB')  
            img.thumbnail((400, 400))  

            thumb_io = BytesIO()
            img.save(thumb_io, format='JPEG', quality=70)

            original_filename = os.path.basename(self.gambar.name) 
            thumb_filename = f"thumb_{original_filename}"

            self.thumbnail.save(f"thumbnails/{thumb_filename}", ContentFile(thumb_io.getvalue()), save=False)

            super().save(update_fields=['thumbnail'])

    def __str__(self):
        return self.judul
