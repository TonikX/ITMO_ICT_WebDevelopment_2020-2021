from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('driver/', get_drivers),
    path('driver/<int:driver_id>/', get_driver),
    path('drivers/', get_drivers),
    path('cars/', CarsListView.as_view()),
    path('car/<int:pk>/', CarDetailView.as_view()),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('driver/create/', create_view),
    path('car/create/', CarCreate.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
]