from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.conf import settings 
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
import requests
import uuid


API_KEY = 'dea08359975947fcadead78bf4b5d704'  

def authenticate_email(email, auth_token):
    subject = 'Your accounts need to be verified IITB ASSIGNMENT'
    email_from = settings.EMAIL_HOST_USER
    reciver_list = [email]
    text_content = 'Please verify your account'
    html_content = f'<p>Please click on the button to verify the account to access IITB ASSIGNMENT<p/><br><a href="http://127.0.0.1:8000/verify/{auth_token}" class="btn btn-primary">Click Here <a/>'
    msg = EmailMultiAlternatives(subject, text_content, email_from, reciver_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def verifyUser(request, auth_token):
    if request.method == 'POST':
        newvar = request.POST.get('url')
        check_token = userProfiles.objects.filter(auth_token = newvar).first()
        if check_token:
            user = User.objects.filter(username = check_token).first()
            user.is_active = True
            user.save()
            return redirect('user-login')
    
    return render(request, 'authUser/emailVerification.html')

def registerUser(request):
    form  = userRegistrationForm()
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        if User.objects.filter(username = username):
            messages.warning(request, 'Username already taken')
        elif User.objects.filter(email = email):
            messages.info(request, 'User already taken with the email')
        elif form.is_valid():
            saveForm = form.save()
            auth_token = str(uuid.uuid4())
            profile = userProfileForm().save(commit=False)
            profile.user = saveForm
            profile.auth_token = auth_token
            profile.save()
            messages.info(request, "Please Verify Your Accounts! Visit the Linke ")
            authenticate_email(email, auth_token)
            return render(request, "authUser/userRegistration.html")
        else: 
            messages.warning(request, "Password mut be atleast 8 characters long and should have a special character and a number")

    context = {
        'form' : form
    }
    return render(request, "authUser/userRegistration.html", context)



def userLogin(request):
    form = loginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            userId = user.id
            isActive = user.is_active
            if isActive:
                login(request, user)
                messages.info(request, "User Successfully Authencitated")  
                return redirect('home')
                
            else:
                messages.info(request, 'Please Verify Your Account')

        else:
            messages.info(request, 'Username or Password Is Incorrect')

    context = {
        'form' : form
    }
    return render(request, "authUser/userLogin.html", context)


@login_required(login_url='user-login')
def home(request):
    url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {
        'data' : data,
        'articles' : articles
    }
    return render(request, "index.html", context)