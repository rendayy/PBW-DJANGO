from django.apps import AppConfig
from django.db import connection
from django.db.utils import OperationalError


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        try:
            connection.ensure_connection()
            print("✅ Berhasil terhubung ke database:", connection.settings_dict['NAME'])
        except OperationalError:
            print("❌ Gagal terhubung ke database")
            
        import app.signals
