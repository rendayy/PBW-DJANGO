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
        # Hapus thumbnail lama jika gambar berubah
        if self.pk:  # Jika objek sudah ada di database
            old = Create.objects.get(pk=self.pk)
            if old.gambar != self.gambar:  # Jika gambar diubah
                old.thumbnail.delete(save=False)  # Hapus file thumbnail lama
                self.thumbnail = None  # Reset reference thumbnail

        super().save(*args, **kwargs)  # Simpan perubahan utama

        # Generate thumbnail baru jika diperlukan
        if self.gambar and (not self.thumbnail or self.thumbnail.name is None):
            img = Image.open(self.gambar)
            img = img.convert('RGB')
            
            # Ukuran thumbnail
            thumbnail_size = (400, 400)
            img.thumbnail(thumbnail_size)

            # Simpan ke buffer
            thumb_io = BytesIO()
            img.save(thumb_io, 'JPEG', quality=70)
            thumb_io.seek(0)

            # Nama file thumbnail
            thumb_name = f"thumb_{os.path.basename(self.gambar.name)}"
            
            # Simpan thumbnail
            self.thumbnail.save(
                f"thumbnails/{thumb_name}",
                ContentFile(thumb_io.read()),
                save=False
            )
            super().save(update_fields=['thumbnail'])  # Simpan field thumbnail saja

    def __str__(self):
        return self.judul
