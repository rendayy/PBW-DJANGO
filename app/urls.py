from django.urls import path
from . import login_register
from .create import upload_view
from .global_post import global_gallery
from app.login_register import home 

urlpatterns = [
    path('', login_register.home, name='home'),
    path('register/', login_register.register_view, name='register'),
    path('login/', login_register.login_view, name='login'),
    path('admin/', login_register.admin_dashboard, name='admin_dashboard'),
    path('staff/', login_register.staff_dashboard, name='staff_dashboard'),
    path('user/', login_register.user_dashboard, name='user_dashboard'),
    path('logout/', login_register.logout_view, name='logout'),
    path('upload/',upload_view, name='upload'),
    path('otp/', login_register.verify_otp, name='otp'),
    path('gallery/', global_gallery, name='gallery'),
]
