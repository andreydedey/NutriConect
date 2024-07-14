from django.http import HttpResponse 
from .models import CustomUser
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth, messages 


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('patients'))

    if request.method == 'GET':
        return render(request, "login/login.html")


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user=user)
            return redirect(reverse('patients'))
        
        messages.add_message(request, messages.constants.WARNING, 'Incorrect username or password')
        return redirect(reverse('login'))


def register(request):
    if request.method == 'GET':
        return render (request, "register/register.html")
    

    if request.method == 'POST':
        # The inspection of the form was done in the client side 
        try:

            username = request.POST.get('username').strip()
            email = request.POST.get('email').strip()
            password = request.POST.get('password').strip()

            user = CustomUser.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect(reverse('login'))
        
        except IntegrityError:
            messages.add_message(request, messages.constants.WARNING, 'username already exists, try another')
            return redirect(reverse('register'))
