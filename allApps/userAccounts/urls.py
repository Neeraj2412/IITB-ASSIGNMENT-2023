from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.userLogin, name='user-login'),
    path('logout/', views.logoutUser, name='user-logout'),
    path('userAccounts/user_profile/', views.userProfile, name='user_profile'),
    path('userAccounts/emailsignup/', views.registerUser, name='user-registration'),
    path('verify/<auth_token>', views.verifyUser, name='verifyUser'),
    path('userAccounts/change_password/', auth_views.PasswordChangeView.as_view(template_name="authUser/changePassword.html"), name="change_password"),
    path('userAccounts/password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name="authUser/passwordChangeDone.html"), name="password_change_done"),
    path('userAccounts/password_reset/', auth_views.PasswordResetView.as_view(template_name="authUser/forgotPassword.html"), name='password_reset'),    
    path('userAccounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="authUser/forgotPasswordEmailSent.html"), name='password_reset_done'),    
    path('userAccounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="authUser/resetPassword.html"), name='password_reset_confirm'),    
    path('userAccounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="authUser/passwordResetComplete.html"), name='password_reset_complete'),    
    path('home/', views.home, name='home'),
]   