from django.urls import path
from . import views as local_views
from posts import views as posts_views


urlpatterns = [
    # personal views
    path('hello', local_views.hello_world),
    path('hi', local_views.hi),
    path('say_hi/<str:name>/<int:age>', local_views.say_hi),

    # app posts views
    path('posts', posts_views.list_posts)
]
