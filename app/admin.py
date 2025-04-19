from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Create

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fields = ('role',)  # Tampilkan hanya field role

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)  # Tambahkan inline Profile
    list_display = ('username', 'email', 'is_staff', 'get_role')
    
    def get_role(self, obj):
        return obj.profile.role
    get_role.short_description = 'Role'

# Unregister dan register kembali
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register Profile juga secara terpisah
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')

@admin.register(Create)
class CreateAdmin(admin.ModelAdmin):
    list_display = ('judul', 'user', 'kategori', 'tanggal_upload', 'status')
    list_filter = ('status', 'tanggal_upload')
    search_fields = ('judul', 'kategori', 'deskripsi', 'user__username')
