from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.userLogin, name='user-login'),
    path('home', views.home, name='home'),
    path('userAccounts/emailsignup/', views.registerUser, name='user-registration'),
    path('verify/<auth_token>', views.verifyUser, name='verifyUser'),
]   