from django.db.models import Prefetch
from rest_framework import viewsets, permissions
from .serializers import *


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = HotelSerializer


class RoomViewGet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Room.objects.all()
        print(queryset)
        hotel = self.request.query_params.get('hotel', None)
        if hotel is not None:
            queryset = queryset.filter(hotel=hotel)
        return queryset

    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomSerializerSet


class BookingViewGet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Booking.objects.all()
        print(queryset)
        room = self.request.query_params.get('room', None)
        guest = self.request.query_params.get('guest', None)
        if room is not None:
            queryset = queryset.filter(room=room)
        elif guest is not None:
            queryset = queryset.filter(guest=guest)
        return queryset

    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()

    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookingSerializerSet


class CommentsViewGet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Comments.objects.all()
        print(queryset)
        hotel = self.request.query_params.get('hotel', None)
        if hotel is not None:
            queryset = queryset.filter(hotel=hotel)
        return queryset
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CommentsSerializerGet


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CommentsSerializerSet
