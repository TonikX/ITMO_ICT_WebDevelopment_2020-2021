from rest_framework import serializers
from .models import *


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ["session", "client"]
        
        
class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ["name", "birthday", "bookings"]
        depth = 2

        
class LessonTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonType
        fields = ["name", "description"]
        
        
class CoachSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coach
        fields = ["name", "description"]


class SessionSerializer(serializers.ModelSerializer):
    lesson_type = serializers.SlugRelatedField(read_only='True', slug_field='name')
    
    class Meta:
        model = LessonSession
        fields = ["weekday", "time", "lesson_type"]
        
        
class SessionByWeekday(serializers.ModelSerializer):
    coach = serializers.SlugRelatedField(read_only='True', slug_field='name')
    lesson_type = LessonTypeSerializer()
    
    class Meta:
        model = LessonSession
        fields = ["time", "coach", "lesson_type"]
        

"""class ProfileSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    booking = BookingSerializer(many=True)

    class Meta:
        model = Client
        fields = "__all__" """
        