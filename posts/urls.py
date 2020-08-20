"""Posts URLs"""

# django
from django.urls import path

# views
from posts import views

urlpatterns = [

    path(
        route = '', 
        view = views.list_posts,
        name = 'feed'),
    
    path(
        route = '/new',
        view = views.create_post,
        name="create"),
]