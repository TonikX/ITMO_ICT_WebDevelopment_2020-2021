

"""ray_system URL Configuration

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
from django.urls import path, include, re_path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('workers', WorkersAPI.as_view()),
    path('auth/token', obtain_jwt_token),
    path('auth/token/refresh', refresh_jwt_token),
    path('applications', ApplicationsAPI.as_view()),
    path('applications/create', ApplicationsCreateAPI.as_view()),
    path('applications/<int:pk>', ApplicationsDetailsAPI.as_view()),
    path('applications/<int:pk>/delete', ApplicationsDeleteAPI.as_view()),
    path('applications/<int:pk>/update', ApplicationsUpdateAPI.as_view()),
    path('service/create', ServiceCreateAPI.as_view()),
    path('service/<int:pk>/update', ServiceUpdateAPI.as_view()),
    path('service', ServiceAPI.as_view()),
    path('service/<int:pk>/delete', ServiceDeleteAPI.as_view()),
    path('service/<int:pk>', ServiceDetailsAPI.as_view()),
    path('assignment/create', AssignmentCreateAPI.as_view()),
    path('assignment/<int:pk>/update', AssignmentUpdateAPI.as_view()),
    path('assignment', AssignmentAPI.as_view()),
    path('assignment/<int:pk>/delete', AssignmentDeleteAPI.as_view()),
    path('assignment/<int:pk>', AssignmentDetailsAPI.as_view()),
]
