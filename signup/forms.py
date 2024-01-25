from django import forms

class CustomSignupForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'inputS', 'placeholder': 'Username', 'required': 'required'})
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'inputS', 'placeholder': 'Email', 'required': 'required'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'inputS', 'placeholder': 'Password', 'required': 'required'})
    )

    gender = forms.ChoiceField(
        choices=[('', 'Select Gender'), ('M', 'Male'), ('F', 'Female')],
        widget=forms.Select(attrs={'class': 'selectG', 'required': 'required'})
    )