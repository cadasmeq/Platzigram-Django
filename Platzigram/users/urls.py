"""Users URLs"""

# django
from django.urls import path

# views
from users import views


urlpatterns = [

    # Managment
    path(
        route = 'profile/login/',
        view = views.LoginView.as_view(),
        name='login'
    ),
    
    path(
        route = 'profile/logout/',
        view = views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        route = 'profile/signup/',
        view = views.SignupView.as_view(),
        name='signup'
    ),

    path(
        route = 'profile/me/update_profile',
        view = views.UpdateProfileView.as_view(),
        name='update'
    ),

    # Posts
    path(
        route = 'profile/<str:username>/',
        view = views.UserDetailView.as_view(),
        name = 'detail'
    ),


]