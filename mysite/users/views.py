from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegistrationForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'users/register.html',{'form':form})

def custom_logout(request):
    logout(request)
    return render(request,'users/logout.html')
@login_required
def profilepage(request):
    return render(request,'users/profile.html')

