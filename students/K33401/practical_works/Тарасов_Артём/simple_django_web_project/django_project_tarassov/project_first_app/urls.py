"""django_project_grigoreva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from project_first_app import views
from project_first_app.views import *

urlpatterns = [
    path('drivers/', views.all_drivers_detail),
    path('driver/<int:driver_id>/', views.driver_detail),
    path('create_driver/', views.create_driver),
    path('cars/', AllCars.as_view()),
    path('car/<int:pk>/', OneCar.as_view()),
    path('car/<int:pk>/update', CarUpdate.as_view()),
    path('car/create/', CarCreate.as_view()),
    path('car/<int:pk>/delete/', CarDelete.as_view()),
]
