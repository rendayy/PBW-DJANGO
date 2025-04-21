from django.contrib import admin
from .models import Create

@admin.register(Create)
class CreateAdmin(admin.ModelAdmin):
    list_display = ('judul', 'user', 'kategori', 'tanggal_upload', 'status')
    list_filter = ('status', 'tanggal_upload')
    search_fields = ('judul', 'kategori', 'deskripsi', 'user__username')
