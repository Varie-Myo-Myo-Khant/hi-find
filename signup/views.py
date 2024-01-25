from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .forms import CustomSignupForm
from .models import lostUser
from django.contrib import messages

def get_signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            # Create a Users instance and save it
            user_profile = lostUser(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password']),  # Hash the password
                gender=form.cleaned_data['gender']
            )
            
            user_profile.save()
            messages.add_message(request, messages.SUCCESS, 'Your Regiration is Successful! Please login to get started.')
            return redirect('login')
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})