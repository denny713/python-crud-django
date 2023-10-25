from django import forms
from .models import Akun


class UserForm(forms.ModelForm):
    class Meta:
        model = Akun
        fields = ['username', 'nama', 'password', 'status']
