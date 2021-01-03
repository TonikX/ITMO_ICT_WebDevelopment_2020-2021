from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields = ['first_name', 'last_name', 'username', 'passport']


class AirlineSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Airline
        fields = ["name"]


class AirportCreateSerializer(serializers.ModelSerializer):
    company = AirlineSerializer()

    class Meta:
        model = Airport
        fields = "__all__"

    def create(self, validated_data):
        airoport = Airport(**validated_data)
        airoport.save()
        return Airport(**validated_data)


class AiraportNestedSerializer(serializers.ModelSerializer):
    # делаем наследование
    company = AirlineSerializer()

    # уточняем поле
    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Airport
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["name"]


class CityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

    def create(self, validated_data):
        city = City(**validated_data)
        city.save()
        return City(**validated_data)


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"


# class RouteCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Route
#         fields = "__all__"
#
#     def create(self, validated_data):
#         route = Route(**validated_data)
#         route.save()
#         return Route(**validated_data)


class ArrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"


# class RouteCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Route
#         fields = "__all__"
#
#     def create(self, validated_data):
#         route = Route(**validated_data)
#         route.save()
#         return Route(**validated_data)


class DepartureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = "__all__"


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = "__all__"


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = "__all__"



