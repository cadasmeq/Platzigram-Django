# django
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

# app
from . import views as local_views
from posts import views as posts_views
from users import views as users_views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('posts', posts_views.list_posts, name='feed'),
    path('account/login', users_views.login_view, name='login'),

    path('hello', local_views.hello_world),
    path('hi', local_views.hi),
    path('say_hi/<str:name>/<int:age>', local_views.say_hi),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
