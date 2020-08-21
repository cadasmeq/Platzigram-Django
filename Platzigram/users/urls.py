"""Users URLs"""

# django
from django.urls import path

# views
from users import views


urlpatterns = [

    path(
        route = 'profile/<str:username>/',
        view = views.UserDetailView.as_view(),
        name = 'detail', 
    ),

    path(
        route = 'profile/login/',
        view = views.login_view,
        name='login'),

    path(
        route = 'profile/logout/',
        view = views.logout_view,
        name='logout'),

    path(
        route = 'profile/signup/',
        view = views.signup_view,
        name='signup'),

    path(
        route = 'profile/me/update_profile',
        view = views.update_profile_view,
        name='update'),

]