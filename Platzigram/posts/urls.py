"""Posts URLs"""

# django
from django.urls import path

# views
from posts import views

urlpatterns = [

    path(
        route = '', 
        view = views.ListPostView.as_view(),
        name = 'feed'),
    
    path(
        route = '/new',
        view = views.create_post,
        name="create"),

    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    )
]