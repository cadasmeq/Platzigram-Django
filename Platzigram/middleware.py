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
            profile = request.user.profile
            if not profile.biography or not profile.picture:
                if request.path != reverse('update'):
                    return redirect('update')
        
        response = self.get_response(request)
        return response


