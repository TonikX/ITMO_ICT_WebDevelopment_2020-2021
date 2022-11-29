  
from django.urls import path, include
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('owner/<int:id>/', detail, name='owner_page_url'),
]