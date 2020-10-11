from django.contrib import admin
from django.urls import path, include

from project_first_app.views import DriverDetailView

urlpatterns = [
    path('driver/<int:pk>', DriverDetailView.as_view())
]
