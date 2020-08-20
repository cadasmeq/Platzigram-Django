"""Users URLs"""

# django
from django.urls import path

# views
from users import views


urlpatterns = [

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