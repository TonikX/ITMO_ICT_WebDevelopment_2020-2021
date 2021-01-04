from django.shortcuts import render
from django.db import models
from rest_framework import generics

from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class AirlineListAPIView(generics.ListAPIView):
    serializer_class = AirlineSerializer
    queryset = Airline.objects.all()


class AirlineCreateAPIView(generics.CreateAPIView):
    serializer_class = AirlineSerializer
    queryset = Airline.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AirportsListAPIView(generics.ListAPIView):
    serializer_class = AiraportNestedSerializer
    queryset = Airport.objects.all()


class AirportCreateAPIView(generics.CreateAPIView):
    serializer_class = AirportCreateSerializer
    queryset = Airport.objects.all()


class CityListAPIView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class CityCreateAPIView(generics.CreateAPIView):
    serializer_class = CityCreateSerializer
    queryset = City.objects.all()


class RouteListAPIView(generics.ListAPIView):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class RouteCreateAPIView(generics.CreateAPIView):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class ArrivalListAPIView(generics.ListAPIView):
    serializer_class = ArrivalSerializer
    queryset = Arrival.objects.all()


class ArrivalCreateAPIView(generics.CreateAPIView):
    serializer_class = ArrivalSerializer
    queryset = Arrival.objects.all()


class DepartureListAPIView(generics.ListAPIView):
    serializer_class = DepartureSerializer
    queryset = Departure.objects.all()


class DepartureCreateAPIView(generics.CreateAPIView):
    serializer_class = DepartureSerializer
    queryset = Departure.objects.all()


class FlightCreateAPIView(generics.CreateAPIView):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()


class FlightListAPIView(generics.ListAPIView):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()


class PlaneListAPIView(generics.ListAPIView):
    serializer_class = PlaneSerializer
    queryset = Plane.objects.all()


class PlaneCreateAPIView(generics.CreateAPIView):
    serializer_class = PlaneSerializer
    queryset = Plane.objects.all()


class BoardListAPIView(generics.ListAPIView):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()


class BoardCreateAPIView(generics.CreateAPIView):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()


class FlightAttendantCreateAPIView(generics.CreateAPIView):
    serializer_class = FlightAttendantSerializer
    queryset = FlightAttendant.objects.all()


class FlightAttendantListAPIView(generics.ListAPIView):
    serializer_class = FlightAttendantSerializer
    queryset = FlightAttendant.objects.all()


class PilotListAPIView(generics.ListAPIView):
    serializer_class = PilotSerializer
    queryset = Pilot.objects.all()


class PilotCreateAPIView(generics.CreateAPIView):
    serializer_class = PilotSerializer
    queryset = Pilot.objects.all()



