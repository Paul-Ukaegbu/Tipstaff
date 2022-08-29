from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns= [
   path('', views.home, name='home'),
   path('', views.login, name ='login'),
   path('', views.signup, name ='signup'),
]