
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Drivers/', views.driverF, name='Drivers'),
    path('Car/', views.CarF, name="Car"),
   # path('addCar/', views.addCar),
    path('create_car', views.CarCreate.as_view(success_url = '/Car/'), name = 'create_car'),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view(success_url = '/Car/')),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view(success_url = '/Car/')),
    path('Possession/', views.PossessionF),
    path('DriverDocument/', views.DriverDocumentF),
    path('addDrivers/', views.addDrivers)
]
