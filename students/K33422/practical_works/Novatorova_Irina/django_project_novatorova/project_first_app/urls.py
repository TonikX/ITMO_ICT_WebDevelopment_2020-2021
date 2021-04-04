from django.urls import path
from . import views

urlpatterns = [
    path('driver/<int:driver_id>/', views.driver),
    path('alldrivers/', views.alldrivers),
    path('add_driver/', views.add_driver),

    path('car/<int:pk>/', views.Car.as_view()),
    path('allcars/', views.Allcars.as_view()),
    path('car/<int:pk>/update/', views.UpdateCar.as_view()),
    path('car/<int:pk>/delete/', views.DeleteCar.as_view()),
    path('add_car/', views.AddCar.as_view()),

]
