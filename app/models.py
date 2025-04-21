from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Create(models.Model):
    STATUS_CHOICES = (
        ('p', 'Pending'),
        ('a', 'Approved'),
        ('r', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gambar = models.ImageField(upload_to='uploads/')
    kategori = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    judul = models.CharField(max_length=200)
    tanggal_upload = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')

    def __str__(self):
        return self.judul