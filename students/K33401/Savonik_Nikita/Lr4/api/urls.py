from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    path('cars/', CarsAPIView.as_view()),
    path('cars/create/', CarsCreateAPIView.as_view()),
    path('cars/<int:pk>/', CarAPIView.as_view()),
    path('cars/<int:pk>/update/', CarUpdateAPIView.as_view()),
    path('cars/<int:pk>/delete/', CarDeleteAPIView.as_view()),
    path('orders/', OrdersAPIView.as_view()),
    path('orders/create/', OrdersCreateAPIView.as_view()),
    path('orders/<int:pk>/', OrderAPIView.as_view()),
    path('orders/<int:pk>/update/', OrderUpdateAPIView.as_view()),
    path('orders/<int:pk>/delete/', OrderDeleteAPIView.as_view()),
    path('car_to_orders/create/', CarToOrderCreateAPIView.as_view()),
    path('car_to_orders/<int:pk>/', CarToOrderAPIView.as_view()),
    path('car_to_orders/<int:pk>/update/', CarToOrderUpdateAPIView.as_view()),
    path('car_to_orders/<int:pk>/delete/', CarToOrderDeleteAPIView.as_view()),
]
