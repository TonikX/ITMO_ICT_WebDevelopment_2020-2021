"""laboratory_work_2 URL Configuration

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
from django.contrib.auth import views
from django.urls import path

from racing_scoreboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('', RaceListView.as_view(), name='race-list'),
    path('registration/', RegistrationListView.as_view(), name='registration-list'),
    path('race/<int:pk>', RaceDetailView.as_view(), name='race-detail'),
    path('racer/<int:pk>', RacerDetailView.as_view(), name='racer-detail'),
    path('racer/update/<int:pk>', RacerUpdateView.as_view(), name='racer-update'),
    path('racer/create/', RacerCreateView.as_view(), name='racer-create'),
]
