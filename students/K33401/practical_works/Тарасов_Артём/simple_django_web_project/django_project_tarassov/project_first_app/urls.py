from django.urls import path
from . import views

urlpatterns = [
    path('drivers/', views.detail),
    path('cars/', views.CarsList.as_view()),
    path('car/<int:pk>/', views.CarDetailView.as_view()),
    path('create_driver/', views.create_driver_view),
    path('create_car/', views.CarCreate.as_view()),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view()),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view()),
]
