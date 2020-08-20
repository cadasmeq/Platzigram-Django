"""Complete user information middleware"""

# django
from django.shortcuts import redirect
from django.urls import reverse

class UserInformationMiddleware:
    """Fill information middleware"""
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.biography or not profile.picture:
                    if request.path != reverse('users:update'):
                        if request.path != reverse('users:logout'):
                            return redirect('users:update')
        
        response = self.get_response(request)
        return response


