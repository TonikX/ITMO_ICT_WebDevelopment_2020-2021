from django.urls import path
from .views import *

urlpatterns = [
    path('pizzas/', PizzasListAPIView.as_view()),
    path('pizzas/create/', PizzasCreateAPIView.as_view()),
    path('pizzas/<int:pk>/', PizzasRetrieveAPIView.as_view()),
    path('pizzas/<int:pk>/update/', PizzasUpdateAPIView.as_view()),
    path('pizzas/<int:pk>/delete/', PizzasDeleteAPIView.as_view()),
    path('orders/', OrderListAPIView.as_view()),
    path('orders/create/', OrderCreateAPIView.as_view()),
    path('orders/<int:pk>/', OrderRetrieveAPIView.as_view()),
    path('orders/<int:pk>/update/', OrderUpdateAPIView.as_view()),
    path('orders/<int:pk>/delete/', OrderDeleteAPIView.as_view()),
    # path('orderedPizzas/', OrderedPizzasListAPIView.as_view()),
    path('orderedPizzas/create/', OrderedPizzasCreateAPIView.as_view()),
    path('orderedPizzas/<int:pk>/', OrderedPizzasRetrieveAPIView.as_view()),
    path('orderedPizzas/<int:pk>/update/', OrderedPizzasUpdateAPIView.as_view()),
    path('orderedPizzas/<int:pk>/delete/', OrderedPizzasDeleteAPIView.as_view()),

]