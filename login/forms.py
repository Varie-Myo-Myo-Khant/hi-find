from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'inputS', 'placeholder': 'Username', 'required': 'required'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'inputS', 'placeholder': 'Password', 'required': 'required'})
    )
    