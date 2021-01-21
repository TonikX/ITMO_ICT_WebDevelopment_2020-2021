from django.contrib import admin
from django.urls import path, include

from project_first_app.views import DriverDetailView, CarsList, CarDetailView, create_driver_view, CarCreate, \
    CarUpdateView, CarDeleteView

urlpatterns = [
    path('driver/<int:pk>', DriverDetailView.as_view()),
    path('car/', CarsList.as_view()),
    path('car/<int:pk>/', CarDetailView.as_view()),
    path('driver/create', create_driver_view),
    path('car/create', CarCreate.as_view()),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
]
