from rest_framework import viewsets, permissions
from .serializers import *


class AirlinesViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = AirlinesSerializer


class CityAirportViewSet(viewsets.ModelViewSet):
    queryset = CityAirport.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CityAirportSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = FlightSerializer


class FlightViewGet(viewsets.ReadOnlyModelViewSet):
    queryset = Flight.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = GetFlightSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Place.objects.all()
        num_flight = self.request.query_params.get('num_flight', None)
        passenger = self.request.query_params.get('passenger', None)
        if num_flight is not None:
            queryset = queryset.filter(num_flight=num_flight)
        elif passenger is not None:
            queryset = queryset.filter(passenger=passenger)
        return queryset

    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlaceSerializer


class PlaceViewGet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        queryset = Place.objects.all()
        num_flight = self.request.query_params.get('num_flight', None)
        passenger = self.request.query_params.get('passenger', None)
        if num_flight is not None:
            queryset = queryset.filter(num_flight=num_flight)
        elif passenger is not None:
            queryset = queryset.filter(passenger=passenger)
        return queryset

    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = GetPlaceSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CommentsSerializer
