from django.contrib.auth.models import User
from django import forms
# from django.contrib.auth.forms import UserModel


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
