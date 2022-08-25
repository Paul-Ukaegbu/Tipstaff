from django.shortcuts import render,redirect

def index(request):
    context = {
        "body": "Hello everyone!"
    }
    return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html')

def signup(response):
    return render(request, 'signup.html')
