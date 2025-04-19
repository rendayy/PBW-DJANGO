import random
import smtplib
from .models import Profile
from .forms import RegisterForm
from django.contrib import messages
from email.message import EmailMessage
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from config.settings import EMAIL_ADDRESS, EMAIL_PASSWORD
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Generate OTP Code
def code_otp():
    otp = "".join(str(random.randint(0, 9)) for _ in range(6))
    return otp

# User Register
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')  
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')  
            
            request.session['username'] = username  
            request.session['email'] = email  
            request.session['password'] = password  

            otp_code = code_otp() 
            request.session['otp'] = otp_code 
            
            if send_otp(otp_code, request):
                request.session['otp_sent'] = True 
                return redirect('otp') 
            else:
                messages.error(request, 'Gagal mengirim OTP. Silakan coba lagi.')
                request.session['otp_sent'] = False 
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# Send OTP
def send_otp(otp_code, request):
    # Ambil email dari sesi
    email = request.session.get('email')  
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        html_content = render_to_string('otp_email.html', {'otp_code': otp_code})

        message = EmailMessage()
        message['Subject'] = 'OTP Verification'
        message['From'] = EMAIL_ADDRESS
        message['To'] = email 

        message.set_content(html_content, subtype='html')
        server.send_message(message)
        server.quit()
        return True
    except Exception as e:
        return False

# Verify OTP
def verify_otp(request):
    if request.method == 'POST':
        user_otp = ''.join(request.POST.get(f"otp{i}") for i in range(1, 7))

        if user_otp == request.session.get('otp'):
            username = request.session.pop('username', None)  
            email = request.session.pop('email', None)  
            password = request.session.pop('password', None) 

            if username and email and password:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    Profile.objects.get_or_create(user=user, defaults={'role': 'user'})
                    user.save()
                    request.session.pop('otp', None) 
                    return redirect('login')
                except Exception as e:
                    messages.error(request, "Terjadi kesalahan saat membuat akun.")
            else:
                messages.error(request, "Data pengguna tidak lengkap.")
        else:
            messages.error(request, "Kode OTP salah. Silakan coba lagi.")
            return render(request, "otp.html")
    return render(request, "otp.html")

# Login
def login_view(request):
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
        else:
            return render(request, 'login.html', {'error': 'Username atau Password salah'})

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

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')
