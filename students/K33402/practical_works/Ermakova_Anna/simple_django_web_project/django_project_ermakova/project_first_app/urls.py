from django.urls import path
from . import views
from .views import CarsList, CarDetail, UpdateCar, AddCar, DeleteCar

urlpatterns = [
    path('owner/', views.owners, name='owners'),
    path('owner/<int:number>', views.owner, name='owner'),
    path('add_person/', views.add_person),
    path('cars/', CarsList.as_view()),
    path('cars/<int:pk>', CarDetail.as_view()),
    path('cars/<int:pk>/update/', UpdateCar.as_view()),
    path('add_car/', AddCar.as_view()),
    path('cars/<int:pk>/delete/', DeleteCar.as_view())
]
