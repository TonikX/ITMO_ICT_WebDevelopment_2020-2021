from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

from . import models
from . import serializers


class Permission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        else:
            return bool(request.user and request.user.is_staff)


######################################################################################################################
######################################################################################################################


class DriverListAPIView(ListCreateAPIView):
    queryset = models.Driver.objects.all()
    serializer_class = serializers.DriverSerializer
    permission_classes = [Permission]


class DriverDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Driver.objects.all()
    serializer_class = serializers.DriverSerializer
    permission_classes = [Permission]


######################################################################################################################


class BusListAPIView(ListCreateAPIView):
    queryset = models.Bus.objects.all()
    serializer_class = serializers.BusSerializer
    permission_classes = [Permission]


class BusDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Bus.objects.all()
    serializer_class = serializers.BusSerializer
    permission_classes = [Permission]


######################################################################################################################


class RoutesListAPIView(ListCreateAPIView):
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer
    permission_classes = [Permission]


class RoutesDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer
    permission_classes = [Permission]


######################################################################################################################


class ShiftsListAPIView(ListCreateAPIView):
    queryset = models.Shift.objects.all()
    serializer_class = serializers.ShiftSerializer
    permission_classes = [Permission]


class ShiftsDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Shift.objects.all()
    serializer_class = serializers.ShiftSerializer
    permission_classes = [Permission]


######################################################################################################################
