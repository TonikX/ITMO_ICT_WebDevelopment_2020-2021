from django.urls import path, include
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('drivers/', all_drivers),
    path('drivers/create', create_driver),
    path('cars/', CarList.as_view()),
    path('cars/<int:pk>', CarDetail.as_view()),
    path('cars/create', CarCreate.as_view()),
    path('cars/<int:pk>/update', CarUpdate.as_view()),
    path('cars/<int:pk>/delete', CarDelete.as_view()),
]