from django.urls import path
from .views import *

app_name = "poultry_farm_app"

urlpatterns = [
    path('users/list/', UserListAPIView.as_view()),
    path('users/info/<int:pk>', UserChangeInfoAPIView.as_view()),
    path('users/add/', UserAddAPIView.as_view()),
    path('chickens/list/', ChickenListAPIView.as_view()),
    path('chickens/info/<int:pk>', ChickenChangeInfoAPIView.as_view()),
    path('chickens/add/', ChickenAddAPIView.as_view()),
    path('breeds/list/', BreedListAPIView.as_view()),
    path('breeds/info/<int:pk>', BreedChangeInfoAPIView.as_view()),
    path('breeds/add/', BreedAddAPIView.as_view()),
    path('service/list/', ServiceListAPIView.as_view()),
    path('service/info/<int:pk>', ServiceChangeInfoAPIView.as_view()),
    path('service/add/', ServiceAddAPIView.as_view()),
    path('cells/list/', CellListAPIView.as_view()),
    path('cells/info/<int:pk>', CellChangeInfoAPIView.as_view()),
    path('cells/add/', CellAddAPIView.as_view()),
    path('service/list/nested/', ServiceNestedAPIView.as_view()),
    path('chickens/list/nested/', ChickenNestedAPIView.as_view()),

 ]