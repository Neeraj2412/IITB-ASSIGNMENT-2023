from django.forms import ModelForm, fields, widgets
from django import forms
from .models import *

class blogsForm(forms.ModelForm):
    class Meta:
        model = blogs
        fields = ['title', 'imageUrl', 'description', 'content']
