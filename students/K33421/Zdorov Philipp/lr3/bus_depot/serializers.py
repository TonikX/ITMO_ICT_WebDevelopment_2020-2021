from rest_framework import serializers
from . import models


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Driver
        fields = '__all__'


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bus
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Route
        fields = '__all__'


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shift
        fields = '__all__'
