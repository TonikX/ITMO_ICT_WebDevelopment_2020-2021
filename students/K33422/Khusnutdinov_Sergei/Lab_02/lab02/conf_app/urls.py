"""lab02 URL Configuration

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
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.main),
    path('profile/', views.profile),
    path('myreserves/', listreserves.as_view(), name='reserves'),
    path('myreserves/myreserves/deletereserve/<int:pk>/', views.deletereserveView.as_view()),
    path('myreserves/myreserves/updatereserve/<int:pk>/', views.updatereserveView.as_view()),
    path('register/', register, name='register'),
    path('confs/', views.confsslist),
    path('confs/<int:pk>/reserve/', CreateReserve.as_view(), name='reserve'),
    path('review/', CreateReview.as_view(), name='review'),
    path('reservedconfs/', views.reservedconfslist),
    path('reviews/', views.reviewslist)
 ]