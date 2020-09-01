from django.urls import path
from . import views


urlpatterns = [
    
    #path services
    
    path('', views.services , name='services'),
    

    ]