from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Create

@login_required
def global_gallery(request):
    query = request.GET.get('search', '')  # Ambil parameter pencarian dari URL
    kategori_filter = request.GET.get('kategori', None)  # Ambil kategori dari URL

    # Ambil semua kategori yang unik
    kategori_list = Create.objects.values_list('kategori', flat=True).distinct()

    if kategori_filter:
        gambar_list = Create.objects.filter(status='a', kategori=kategori_filter).order_by('-tanggal_upload')
    elif query:
        gambar_list = Create.objects.filter(status='a', judul__icontains=query).order_by('-tanggal_upload')
    else:
        gambar_list = Create.objects.filter(status='a').order_by('-tanggal_upload')
    
    return render(request, 'global_post.html', {
        'gambar_list': gambar_list,
        'query': query,
        'kategori_list': kategori_list,
        'kategori_filter': kategori_filter,
    })
