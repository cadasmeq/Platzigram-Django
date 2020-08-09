from django.urls import path
from . import views


urlpatterns = [
    # personal views
    path('hello', views.hello_world)
     
]
