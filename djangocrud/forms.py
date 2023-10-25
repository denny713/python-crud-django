from django import forms
from .models import Akun


class UserForm(forms.ModelForm):
    class Meta:
        model = Akun
        field = ['username', 'nama', 'password', 'status']
