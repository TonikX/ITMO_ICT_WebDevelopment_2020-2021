from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = AirlineSerializer

class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = AiraportNestedSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class =CitySerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = RouteSerializer


class ArrivalViewSet(viewsets.ModelViewSet):
    queryset = Arrival.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ArrivalSerializer


class DepartureViewSet(viewsets.ModelViewSet):
    queryset = Departure.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = DepartureSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = FlightSerializer


class PlaneViewSet(viewsets.ModelViewSet):
    queryset = Plane.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlaneSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = BoardSerializer


class FlightAttendantViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = FlightSerializer


class PilotViewSet(viewsets.ModelViewSet):
    queryset = Pilot.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PilotSerializer