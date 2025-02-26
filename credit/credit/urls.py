"""credit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
  
   path('myapp/', include('myapp.urls')), 


]'''
from django.contrib import admin
from django.urls import path, include
from myapp.views import home,success,forms,tc,details#,credit_card_application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('registration', home, name='home'),
    path('',forms, name='forms'),
    path('success',success, name='success'),
    path('terms and conditions',tc, name='t&c'),
    path('user details',details, name='details'),
   # path('suc',credit_card_application, name='credit_card_application')
    
]



