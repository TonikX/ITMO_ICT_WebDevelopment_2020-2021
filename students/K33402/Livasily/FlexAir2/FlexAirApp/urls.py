from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/list/', UserListAPIView.as_view()),
    path('users/info/<int:pk>', UserInfoAPIView.as_view()),
    path('users/create/', UserCreateAPIView.as_view()),
    path('Airlane/', AirlineListAPIView.as_view()),
    path('Airlane/create/', AirlineCreateAPIView.as_view()),
    path('Airport/list/', AirportsListAPIView.as_view()),
    path('Airport/create/', AirportCreateAPIView.as_view()),
    path('City/list/', CityListAPIView.as_view()),
    path('City/create/', CityCreateAPIView.as_view()),
    path('route/list/', RouteListAPIView.as_view()),
    path('route/create/', RouteCreateAPIView.as_view()),
    path('Arrival/list/', ArrivalListAPIView.as_view()),
    path('Arrival/create/', ArrivalCreateAPIView.as_view()),
    path('Departure/list/', DepartureListAPIView.as_view()),
    path('Departure/create/', DepartureCreateAPIView.as_view()),
    path('Flight/create/', FlightCreateAPIView.as_view()),
    path('Flight/list/', FlightListAPIView.as_view()),
    path('Plane/list/', PlaneListAPIView.as_view()),
    path('Plane/create/', PlaneCreateAPIView.as_view()),
    path('Board/list/', BoardListAPIView.as_view()),
    path('Board/create/', BoardCreateAPIView.as_view()),
    path('FlightAttendant/list/', FlightAttendantListAPIView.as_view()),
    path('FlightAttendant/create/', FlightAttendantCreateAPIView.as_view()),
    path('Pilot/create/', PilotCreateAPIView.as_view()),
    path('Pilot/list/', PilotListAPIView.as_view()),
]

#Описать эндпоинты