from multiprocessing import context
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

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
