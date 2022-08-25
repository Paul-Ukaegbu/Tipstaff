from django.contrib import admin
from django.urls import path
from tipstaff import views as v
from . import views

urlpatterns= [
   path('', views.index, name='index'),
   path('admin/', admin.site.urls),
   path('login/', v.login, name='login'),
   path('signup/', v.signup, name='signup'),
]