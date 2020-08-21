# django
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

# local_views
from . import views as local_views



urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')),

    path('', include(('users.urls', 'users'), namespace='profile')),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
