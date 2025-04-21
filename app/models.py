from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'), 
        ('user', 'User'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    
class Create(models.Model):
    STATUS_CHOICES = (
        ('p', 'Pending'),
        ('a', 'Approved'),
        ('r', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gambar = models.ImageField(upload_to='uploads/')
    thumbnail = models.ImageField(upload_to='uploads/thumbnails/', blank=True, null=True)
    kategori = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    judul = models.CharField(max_length=200)
    tanggal_upload = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.gambar and not self.thumbnail:
            img = Image.open(self.gambar)
            img = img.convert('RGB')  # pastikan dalam mode RGB
            img.thumbnail((400, 400))  # max width/height

            thumb_io = BytesIO()
            img.save(thumb_io, format='jpeg', quality=70)  # kompresi di sini

            thumb_name = f"thumb_{self.gambar.name.split('/')[-1]}"
            self.thumbnail.save(thumb_name, ContentFile(thumb_io.getvalue()), save=False)

            super().save(update_fields=['thumbnail'])  

    def __str__(self):
        return self.judul