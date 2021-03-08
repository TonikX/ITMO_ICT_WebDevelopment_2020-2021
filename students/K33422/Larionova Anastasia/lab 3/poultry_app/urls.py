from django.urls import path
from .views import *

app_name = "poultry_app"

urlpatterns = [
    path('users/list/', UserListAPIView.as_view()),
    path('users/info/<int:pk>', UserInfoAPIView.as_view()),
    path('users/create/', UserCreateAPIView.as_view()),

    path('chickens/list/', ChickenListAPIView.as_view()),
    path('chickens/info/<int:pk>', ChickenInfoAPIView.as_view()),
    path('chickens/create/', ChickenCreateAPIView.as_view()),

    path('breeds/list/', BreedListAPIView.as_view()),
    path('breeds/info/<int:pk>', BreedInfoAPIView.as_view()),
    path('breeds/create/', BreedCreateAPIView.as_view()),

    path('service/list/', ServiceListAPIView.as_view()),
    path('service/info/<int:pk>', ServiceInfoAPIView.as_view()),
    path('service/create/', ServiceCreateAPIView.as_view()),

    path('cells/list/', CellListAPIView.as_view()),
    path('cells/info/<int:pk>', CellInfoAPIView.as_view()),
    path('cells/create/', CellCreateAPIView.as_view()),

    path('service/list/nested/', ServiceNestedAPIView.as_view()),
    path('chickens/list/nested/', ChickenNestedAPIView.as_view()),

 ]