from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *
from .api import *

router = routers.DefaultRouter()
router.register('users', UsersViewSet, 'users')
router.register('airline', AirlineViewSet, 'airline')
router.register('airport', AirportViewSet, 'airport')
router.register('city', CityViewSet, 'city')
router.register('route', RouteViewSet, 'route')
router.register('arrival', ArrivalViewSet, 'arrival')
router.register('departure', DepartureViewSet, 'departure')
router.register('flight', FlightViewSet, 'flight')
router.register('plane', PlaneViewSet, 'plane')
router.register('board', BoardViewSet, 'board')
router.register('flightAttendant', FlightAttendantViewSet, 'flightAttendant')
router.register('pilot', PilotViewSet, 'pilot')


urlpatterns = router.urls
#
# urlpatterns = [
#     path('users/list/', UserListAPIView.as_view()),
#     path('users/info/<int:pk>', UserInfoAPIView.as_view()),
#     path('users/create/', UserCreateAPIView.as_view()),
#     path('Airlane/', AirlineViewSet, 'airline'),
#     path('Airlane/create/', AirlineCreateAPIView.as_view()),
#     path('Airport/list/', AirportsListAPIView.as_view()),
#     path('Airport/create/', AirportCreateAPIView.as_view()),
#     path('City/list/', CityListAPIView.as_view()),
#     path('City/create/', CityCreateAPIView.as_view()),
#     path('route/list/', RouteListAPIView.as_view()),
#     path('route/create/', RouteCreateAPIView.as_view()),
#     path('Arrival/list/', ArrivalListAPIView.as_view()),
#     path('Arrival/create/', ArrivalCreateAPIView.as_view()),
#     path('Departure/list/', DepartureListAPIView.as_view()),
#     path('Departure/create/', DepartureCreateAPIView.as_view()),
#     path('Flight/create/', FlightCreateAPIView.as_view()),
#     path('Flight/list/', FlightListAPIView.as_view()),
#     path('Plane/list/', PlaneListAPIView.as_view()),
#     path('Plane/create/', PlaneCreateAPIView.as_view()),
#     path('Board/list/', BoardListAPIView.as_view()),
#     path('Board/create/', BoardCreateAPIView.as_view()),
#     path('FlightAttendant/list/', FlightAttendantListAPIView.as_view()),
#     path('FlightAttendant/create/', FlightAttendantCreateAPIView.as_view()),
#     path('Pilot/create/', PilotCreateAPIView.as_view()),
#     path('Pilot/list/', PilotListAPIView.as_view()),
# ]
#
# #Описать эндпоинты