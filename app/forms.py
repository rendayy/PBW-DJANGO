from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Create

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateForm(forms.ModelForm):
    class Meta:
        model = Create
        fields = ['gambar','judul','kategori','deskripsi']
