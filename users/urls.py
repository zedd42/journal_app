""" urls for users """
from django.urls import path, include
from . import views
app_name = 'users'
urlpatterns = [
    # include def auth urls
    path('', include('django.contrib.auth.urls')),
    # registeration page
    path('regiter/', views.register, name='register'),
]