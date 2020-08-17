# django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    """User login view"""
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            error = "Invalid User or Password."
            return render(request, "users/login.html", {'error':error})

    return render(request, "users/login.html")
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
