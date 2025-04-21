import random
import smtplib
from .forms import RegisterForm
from django.contrib import messages
from email.message import EmailMessage
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.models import Group, User
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
        # Cleaner OTP collection
        user_otp = ''.join([request.POST.get(f'otp{i}', '') for i in range(1, 7)])
        
        if user_otp == request.session.get('otp'):
            # Get all session data at once
            user_data = {
                'username': request.session.pop('username', None),
                'email': request.session.pop('email', None),
                'password': request.session.pop('password', None)
            }
            
            if None in user_data.values():
                missing = [k for k, v in user_data.items() if v is None]
                messages.error(request, f"Missing data: {', '.join(missing)}")
                return render(request, "otp.html")
            
            try:
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=user_data['password']
                )
                
                # Simplified group assignment
                user_group, _ = Group.objects.get_or_create(name='user')
                user.groups.add(user_group)
                
                # Clean up
                request.session.pop('otp', None)
                login(request, user)
                
                messages.success(request, "Registration successful!")
                return redirect('home')
                
            except IntegrityError:
                messages.error(request, "Username already exists")
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
        else:
            messages.error(request, "Invalid OTP code")
    
    return render(request, "otp.html")


# Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            if user.is_staff:
                return redirect('/admin/')
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Username atau password salah'})
    return render(request, 'login.html')

@login_required
def admin_dashboard(request):
    if not request.user.groups.filter(name='aadmin').exists():  # Modifikasi ini
        return redirect('access_denied')
    return render(request, 'admin_dashboard.html')

@login_required
def staff_dashboard(request):
    if not request.user.groups.filter(name='sstaff').exists():  # Modifikasi ini
        return redirect('access_denied')
    return render(request, 'staff_dashboard.html')

@login_required
def user_dashboard(request):
    """View for regular user dashboard"""
    if not request.user.groups.filter(name='user').exists():
        return redirect('access_denied')
    return render(request, 'user_dashboard.html')

@login_required
def home(request):
    """
    Home page view that shows different content based on user role
    """
    context = {
        'user': request.user,
        'is_admin': request.user.groups.filter(name='admin').exists(),
        'is_staff': request.user.groups.filter(name='staff').exists(),
        'is_regular_user': request.user.groups.filter(name='user').exists()
    }
    return render(request, 'home.html', context)

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')
