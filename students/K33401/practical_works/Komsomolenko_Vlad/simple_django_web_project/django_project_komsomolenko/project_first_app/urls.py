from django.urls import path
from . import  views

urlpatterns = [
    path('owners/', views.owner, name='owner'),
    path('owner/<int:pk>/', views.owner_id.as_view()),
    path('cars/', views.car.as_view()),
    path('car/<int:pk>/', views.car_id.as_view()),
    path('car/update/<int:pk>/', views.car_Update.as_view()),
    path('create_owner/', views.owner_create),
    path('car/delete/<int:pk>/', views.car_delete.as_view()),
    path('cars/create/', views.car_add.as_view()),
]