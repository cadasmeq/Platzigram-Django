"""User App Views"""

# django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# models
from users.models import Profile

# errors
from django.db.utils import IntegrityError

# forms
from users.forms import UpdateForm, SignupForm

def update_profile_view(request):
    """Update user profile view"""
    
    profile = request.user.profile
    if request.method == 'POST':

        form = UpdateForm(request.POST, request.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
     
            profile.website = data['website']
            profile.picture = data['picture']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.save()
            
    else:
        form = UpdateForm()    


    return render(
        request,
        'users/update_profile.html',
        {
            "profile": profile,
            "user": request.user,
            "form": form,

        }
    )

def login_view(request):
    """User login view"""
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts:feed')
        else:
            error = "Invalid User or Password."
            return render(request, "users/login.html", {'error':error})

    return render(request, "users/login.html")

def signup_view(request):
    """Signup new user view"""

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
        request, 
        'users/signup.html',
        {'form':form})

@login_required
def logout_view(request):
    """Logout user view"""
    logout(request)
    return redirect('users:login')
