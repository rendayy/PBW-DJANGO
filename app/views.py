from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Username atau Password salah'})

    return render(request, 'login.html')

@login_required(login_url='login')
def dashboard_view(request):
    if request.user.is_staff:  # Admin
        return render(request, 'admin_dashboard.html')
    else:  # User biasa
        return render(request, 'user_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
