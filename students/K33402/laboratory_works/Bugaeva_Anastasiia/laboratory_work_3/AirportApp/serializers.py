from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]


class AirlinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = "__all__"


class CityAirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityAirport
        fields = "__all__"


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentsForFlightSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ["rating", "author", "text"]


class GetPlaceSerializer(serializers.ModelSerializer):
    passenger = UserSerializer()

    class Meta:
        model = Place
        fields = "__all__"
        depth = 2


class GetPlaceForFlightSerializer(serializers.ModelSerializer):
    passenger = UserSerializer()

    class Meta:
        model = Place
        fields = ["passenger"]


class GetFlightSerializer(serializers.ModelSerializer):
    arrival = CityAirportSerializer(read_only=True)
    departure = CityAirportSerializer(read_only=True)
    company = AirlinesSerializer(read_only=True)
    numberFlight = GetPlaceForFlightSerializer(many=True, read_only=True)
    Flight = CommentsForFlightSerializer(many=True)

    class Meta:
        model = Flight
        fields = "__all__"
