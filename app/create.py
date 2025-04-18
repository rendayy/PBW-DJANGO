# create.py
from django.shortcuts import render, redirect
from .forms import CreateForm

def handle_create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateForm()

    return render(request, 'upload.html', {'form': form})