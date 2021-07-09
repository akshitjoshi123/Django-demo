from os import name
from django.urls import path
from appAuth import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.loginUser, name='login'),
    path('logout',views.logoutUser, name='logout'),
    path('registration',views.registration, name='registration')
]
