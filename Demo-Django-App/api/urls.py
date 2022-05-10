from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.getRoutes),
    path('meetups/', views.getMeetups),
    path('meetup/<int:id>', views.getMeetup),
    path('meetups/register', views.registrationView),
    path('meetups/login', obtain_auth_token)
]