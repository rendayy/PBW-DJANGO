from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Create
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class CreateForm(forms.ModelForm):
    class Meta:
        model = Create
        fields = ['gambar','judul','kategori','deskripsi']
