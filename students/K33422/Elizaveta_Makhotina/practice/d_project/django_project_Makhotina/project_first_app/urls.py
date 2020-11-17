from django.urls import path
from . import views

urlpatterns = [
    path('owner/', views.owners),
    path('owner/<int:pk>', views.OwnerDetails.as_view()),
    path('cars/', views.Cars.as_view()),
    path('cars/<int:pk>', views.CarDetails.as_view()),
    path('create_owner/', views.create_owner),
    path('cars/create_car/', views.create_car.as_view(success_url='/cars/')),
    path('cars/<int:pk>/update/', views.update_car.as_view(success_url='/cars/')),
    path('cars/<int:pk>/delete/', views.delete_car.as_view())
]
