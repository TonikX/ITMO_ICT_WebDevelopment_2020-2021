from django.urls import path
from . import views

urlpatterns = [
path('owner/', views.owners),
path('owner/<int:pk>', views.OwnerDetails.as_view()),
path('cars/', views.Cars.as_view()),
path('cars/<int:pk>', views.CarDetails.as_view()),
path('create_owner/', views.create_owner),
path('cars/create_car/', views.CreateCar.as_view(success_url='/cars/')),
path('cars/<int:pk>/update/', views.UpdateCar.as_view(success_url='/cars/')),
path('cars/<int:pk>/delete/', views.DeleteCar.as_view())]
