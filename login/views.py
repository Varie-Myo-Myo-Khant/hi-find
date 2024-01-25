from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomLoginForm
from signup.models import lostUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # Import messages framework

def get_login(request):

    
    if request.method =='POST':
        form= CustomLoginForm(request.POST)
        if form.is_valid():
            luser=form.cleaned_data['username']
            lpassword=form.cleaned_data['password']
            auth = authenticate(request, username=luser, password=lpassword)
            if auth is not None:
                login(request, auth)
                messages.add_message(request, messages.SUCCESS, 'Successfully Logged in!!')
                #Redierct to lost post overall page if successful
                return redirect('Lost Post Overall')
    else:
        form=CustomLoginForm()

    return render(request, 'login.html', {'form': form})
        