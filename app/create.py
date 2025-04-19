from .models import Create
from .forms import CreateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect  # ← tambahkan redirect


@login_required
def upload_view(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('gallery')  # ← ubah sesuai nama URL tujuan
    else:
        form = CreateForm()
    return render(request, 'upload.html', {'form': form})
