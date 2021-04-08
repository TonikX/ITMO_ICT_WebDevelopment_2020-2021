from rest_framework import serializers
from .models import *


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)

    class Meta:
        model = Room
        fields = "__all__"


class RoomSerializerSet(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = "__all__"


class BookingSerializerSet(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')


class CommentsSerializerGet(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    hotel = HotelSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = "__all__"


class CommentsSerializerSet(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = "__all__"
