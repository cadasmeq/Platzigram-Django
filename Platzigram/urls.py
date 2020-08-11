# django
from django.contrib import admin
from django.urls import path

# app
from . import views as local_views
from posts import views as posts_views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('hello', local_views.hello_world),
    path('hi', local_views.hi),
    path('say_hi/<str:name>/<int:age>', local_views.say_hi),
    path('posts', posts_views.list_posts)
]
