from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Profile

# Registrasi
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()  # Simpan user dulu
            
            # Gunakan get_or_create untuk hindari duplikat
            Profile.objects.get_or_create(user=user, defaults={'role': 'user'})
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login dengan Redirect Role
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'profile'):  # Pastikan profile ada
                if user.profile.role == 'admin':
                    return redirect('admin_dashboard')  # Gunakan nama URL pattern, bukan file template
                elif user.profile.role == 'staff':
                    return redirect('staff_dashboard')
            return redirect('user_dashboard')  # Default redirect
    return render(request, 'login.html')

@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')

@login_required
def admin_dashboard(request):
    if request.user.profile.role != 'admin':
        return redirect('access_denied')
    return render(request, 'admin_dashboard.html')

@login_required
def staff_dashboard(request):
    if request.user.profile.role != 'staff':
        return redirect('access_denied')
    return render(request, 'staff_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
