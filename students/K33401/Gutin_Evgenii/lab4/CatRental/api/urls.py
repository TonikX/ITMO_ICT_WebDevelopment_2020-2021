from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    path('cats/', CatsAPIView.as_view()),
    path('cats/create/', CatsCreateAPIView.as_view()),
    path('cats/<int:pk>/', CatAPIView.as_view()),
    path('cats/<int:pk>/update/', CatUpdateAPIView.as_view()),
    path('cats/<int:pk>/delete/', CatDeleteAPIView.as_view()),
    path('ownercats/', OwnerCatsAPIView.as_view()),
    path('orders/', OrdersAPIView.as_view()),
    path('orders/create/', OrdersCreateAPIView.as_view()),
    path('orders/<int:pk>/', OrderAPIView.as_view()),
    path('orders/<int:pk>/update/', OrderUpdateAPIView.as_view()),
    path('orders/<int:pk>/delete/', OrderDeleteAPIView.as_view()),
    path('cat_to_orders/create/', CatToOrderCreateAPIView.as_view()),
    path('cat_to_orders/<int:pk>/', CatToOrderAPIView.as_view()),
    path('cat_to_orders/<int:pk>/update/', CatToOrderUpdateAPIView.as_view()),
    path('cat_to_orders/<int:pk>/delete/', CatToOrderDeleteAPIView.as_view()),
]
