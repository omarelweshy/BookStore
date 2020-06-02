from django.urls import path
from .views import *

urlpatterns = [
    path('about/', HomePageView.as_view(), name='home'),
    path('', AboutPageView.as_view(), name='about'),
        
]
