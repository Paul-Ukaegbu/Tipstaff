from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def index(request):
    context = {
        "body": "Hello everyone!"
    }
    return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html')

def signup(response):
    return render(response, 'signup.html', {"form": form})
