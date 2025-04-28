import random
import smtplib
from .forms import RegisterForm
from django.contrib import messages
from email.message import EmailMessage
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from .models import Create
from .forms import CreateForm 
from django.shortcuts import render, redirect, get_object_or_404
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
    username = request.session.get('username')  # Get the username from the session
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Pass the username to the email template context
        html_content = render_to_string('otp_email.html', {'otp_code': otp_code, 'username': username})

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
                return redirect('login')
                
            except IntegrityError:
                messages.error(request, "Username already exists")
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
        else:
            messages.error(request, "Invalid OTP code")
    
    return render(request, "otp.html")


# Login
def login_view(request):
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
            return redirect('user_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Username atau password salah'})
    return render(request, 'login.html')

@login_required
def admin_dashboard(request):
    if not request.user.groups.filter(name='admin').exists():  # Modifikasi ini
        return redirect('access_denied')
    return render(request, 'admin_dashboard.html')

@login_required
def staff_dashboard(request):
    if not request.user.groups.filter(name='staff').exists():  # Modifikasi ini
        return redirect('access_denied')
    return render(request, 'staff_dashboard.html')

@login_required
def user_dashboard(request):
    # Ambil semua postingan user yang login
    user_posts = Create.objects.filter(user=request.user).order_by('-tanggal_upload')
    
    # Hitung statistik
    total_posts = user_posts.count()
    approved_posts = user_posts.filter(status='a').count()
    pending_posts = user_posts.filter(status='p').count()
    rejected_posts = user_posts.filter(status='r').count()
    
    return render(request, 'user_dashboard.html', {
        'user_posts': user_posts,
        'total_posts': total_posts,
        'approved_posts': approved_posts,
        'pending_posts': pending_posts,
        'rejected_posts': rejected_posts,
    })

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Create, id=post_id, user=request.user)
    
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('user_dashboard')
    else:
        form = CreateForm(instance=post)
    
    return render(request, 'edit_post.html', {
        'form': form,
        'post': post  # Kirim post object ke template
    })

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Create, id=post_id, user=request.user)
    post.delete()
    return redirect('user_dashboard')


# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

def custom_admin_logout(request):
    logout(request)
    return redirect('login')  # Ganti dengan nama URL login Anda