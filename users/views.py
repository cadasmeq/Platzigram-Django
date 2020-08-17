# django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile

# errors
from django.db.utils import IntegrityError

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

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        password_confirm = request.POST['passwd_confirm']

        if password != password_confirm:
            return render(request, 'users/signup.html', {'error':'Password doesnt match'})

        try:
            user = User.objects.create_user(username=username, password=password)

        except IntegrityError:
            return render(request, 'users/signup.html', {'error':'User already exists.'})

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        profile = Profile(user=user)
        profile.save()

        return render(request, 'users/login.html', {'alert':'User created successfuly!'})

    return render(request, 'users/signup.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
