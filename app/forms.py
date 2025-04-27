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
        fields = ['gambar', 'judul', 'kategori', 'deskripsi']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gambar'].required = False  # Gambar tidak wajib di-update

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data['gambar']:  # Jika upload gambar baru
            instance.gambar = self.cleaned_data['gambar']
        elif 'gambar-clear' in self.data:  # Jika hapus gambar
            instance.gambar = None
        if commit:
            instance.save()
        return instance
