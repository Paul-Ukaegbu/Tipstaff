from django.shortcuts import render,redirect
from django.template import Context



def home(request):
    firstName = "Paul"
    lastName = "Ukaegbu"
    post = request.GET.get('textN')
    context = {
        "firstName": firstName,
        "lastName": lastName,
        "post": post
        }
    return render(request, 'tipstaff/home.html', context)
################ login forms ###################################################
def login(request):
    firstName = "Shaniel"
    lastName = "Rivas Verdejo"
    post = request.GET.get('textN')
    context = {
        "firstName": firstName,
        "lastName": lastName,
        "post": post
        }
    return render(request, 'tipstaff/login.html', context)
################ signup forms ###################################################
def signup(request):
    firstName = "Shaniel"
    lastName = "Rivas Verdejo"
    post = request.GET.get('textN')
    context = {
        "firstName": firstName,
        "lastName": lastName,
        "post": post
        }
    return render(request, 'tipstaff/signup.html', context)