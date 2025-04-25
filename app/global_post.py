from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Create

@login_required
def global_gallery(request):
    gambar_list = Create.objects.filter(status='a').order_by('-tanggal_upload')
    return render(request, 'global_post.html', {'gambar_list': gambar_list})

