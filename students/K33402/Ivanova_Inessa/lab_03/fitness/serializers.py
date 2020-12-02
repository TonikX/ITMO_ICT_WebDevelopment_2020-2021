from rest_framework import serializers
from .models import *


class Lessons(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ["name", "description"]
        
        
class Coaches(serializers.ModelSerializer):

    class Meta:
        model = Coach
        fields = ["name", "description"]


class Sessions(serializers.ModelSerializer):
    lesson = serializers.SlugRelatedField(read_only='True', slug_field='name')
    
    class Meta:
        model = Session
        fields = ["weekday", "time", "lesson"]
        
        
class SessionByWeekday(serializers.ModelSerializer):
    coach = serializers.SlugRelatedField(read_only='True', slug_field='name')
    lesson = Lessons()
    
    class Meta:
        model = Session
        fields = ["time", "coach", "lesson"]


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"
        
        
class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"