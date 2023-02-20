from django.forms import ModelForm, fields, widgets
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import *

class userRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
    label="Password",
    widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Confirm Password'}),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'First Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Email'}),
        }


class userProfileForm(forms.ModelForm):
    class Meta:
        model = userProfiles
        fields = ['userProfileImage', 'gender', 'auth_token']

class loginForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Username'}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Password'}),
    )
    class Meta:
        model = User
        fields = ['username', 'password']



