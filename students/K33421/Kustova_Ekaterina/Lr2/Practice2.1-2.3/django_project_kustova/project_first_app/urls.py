from django.urls import path
from project_first_app import views
from .views import owners, car, add_owners
from .views import Cars, CarsUpdate, CarsCreate, CarsDelete

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner),
    path('owners/', owners),
    path('cars/', Cars.as_view()),
    path('car/<int:car_id>/', views.car),
    path('car/<int:pk>/update/', CarsUpdate.as_view()),
    path('add_car/', CarsCreate.as_view()),
    path('car/<int:pk>/delete/', CarsDelete.as_view()),
    path('owner_add/', add_owners),
]
