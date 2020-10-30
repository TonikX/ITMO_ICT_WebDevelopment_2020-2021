from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('owner/<int:id>/', views.get_owner_data),
    path('fun_owners_list/', views.get_all_owners),
    path('cars_list/', GetAllCars.as_view(), name='cars_list'),
    path('add_owner/', views.add_owner),
    path('add_car/', AddCar.as_view()),
    path('car/<int:pk>/', GetCarData.as_view(), name='car_data'),
    path('car/<int:pk>/update', UpdateCar.as_view()),
    path('car/<int:pk>/delete', DeleteCar.as_view())
]
