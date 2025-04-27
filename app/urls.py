from django.urls import path
from . import login_register
from .create import upload_view
from .global_post import global_gallery
from .leanding_page import landing_page
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('register/', login_register.register_view, name='register'),
    path('login/', login_register.login_view, name='login'),
    path('admin/', login_register.admin_dashboard, name='admin_dashboard'),
    path('staff/', login_register.staff_dashboard, name='staff_dashboard'),
    path('user/', login_register.user_dashboard, name='user_dashboard'),
    path('post/edit/<int:post_id>/', login_register.edit_post, name='edit_post'),
    path('post/delete/<int:post_id>/', login_register.delete_post, name='delete_post'),
    path('logout/', login_register.logout_view, name='logout'),
    path('upload/', upload_view, name='upload'),
    path('otp/', login_register.verify_otp, name='otp'),
    path('gallery/', global_gallery, name='gallery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^uploads/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]