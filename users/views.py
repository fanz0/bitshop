from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .forms import ProfileForm

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.success(request, ('There was an error loggin in, try again..'))
            return redirect('login_user')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You were logged out!'))
    return redirect('home_page')

@login_required
def profile(request):
    profile_user = Profile.objects.get(user=request.user)
    profile_bio = profile_user.bio
    profile_wallet = profile_user.wallet_address
    return render(request, 'users/profile.html', {'bio':profile_bio, 'wallet':profile_wallet})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successfull!"))
            profile = Profile()
            profile.user = request.user
            profile.save()
            return redirect('home_page')
    else:
        form = UserCreationForm()
    return render(request, 'authenticate/register_user.html', {'form':form})

def update_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'users/update_profile.html', {'profile':profile, 'form':form})