from django.urls import path
from .views import home

urlpatterns = [
    path('myapp apply/', home, name='home'),  
]


