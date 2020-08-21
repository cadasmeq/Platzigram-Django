"""Users URLs"""

# django
from django.urls import path
from django.views.generic import TemplateView

# views
from users import views


urlpatterns = [

    path(
        route = 'users/<str:username>/',
        view = TemplateView.as_view(
            template_name='users/detail.html'
        ),
        name = 'detail',
        
    ),

    path(
        route = 'users/login/',
        view = views.login_view,
        name='login'),

    path(
        route = 'users/logout/',
        view = views.logout_view,
        name='logout'),

    path(
        route = 'users/signup/',
        view = views.signup_view,
        name='signup'),

    path(
        route = 'users/me/update_profile',
        view = views.update_profile_view,
        name='update'),

]