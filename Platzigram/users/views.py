"""User App Views"""

# django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# views
from django.views.generic import FormView, UpdateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView

# models
from users.models import Profile
from posts.models import Post
from django.contrib.auth.models import User

# forms
from users.forms import UpdateForm, SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""
    
    template_name = "users/detail.html"
    slug_field = 'username'                 # campo slug de la bd
    slug_url_kwarg = 'username'             # campo slug enviado por la url <str:'username'>
    queryset = User.objects.all()
    contex_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')

        return context

class SignupView(FormView):
    """Users Signup View"""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update Profile View"""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'phone_number', 'biography', 'picture']

    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile
    
    def get_success_url(self):
        """Reteurns to user's profile"""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username':username})
    
class LogoutView(LoginRequiredMixin, LogoutView):
    """Logout view."""

    template_name = 'users/login.html'


class LoginView(LoginView):
    """Login view."""

    template_name = 'users/login.html'

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

@login_required
def logout_view(request):
    """Logout user view"""
    logout(request)
    return redirect('users:login')
