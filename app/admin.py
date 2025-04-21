from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Create
from django.utils.html import format_html

@admin.register(Create)
class CreateAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'image_preview')
    list_display = ('judul', 'user', 'kategori', 'tanggal_upload', 'status')
    list_filter = ('status', 'tanggal_upload')
    search_fields = ('judul', 'kategori', 'deskripsi', 'user__username')

    fields = ('user', 'image_preview', 'gambar', 'kategori', 'deskripsi', 'judul', 'status')

    def image_preview(self, obj):
        if obj.gambar:
            return format_html('<img src="{}" style="max-height: 200px;" />', obj.gambar.url)
        return "No image uploaded"
    
    image_preview.short_description = 'Preview Gambar'