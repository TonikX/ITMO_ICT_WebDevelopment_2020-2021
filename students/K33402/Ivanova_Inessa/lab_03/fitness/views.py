from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from drf_multiple_model.views import ObjectMultipleModelAPIView
import requests

class LessonsAPIView(generics.ListAPIView):
    serializer_class = Lessons
    queryset = Lesson.objects.all()
    
    
class CoachesAPIView(generics.ListAPIView):
    serializer_class = Coaches
    queryset = Coach.objects.all()
    

class SessionsAPIView(generics.ListAPIView):
    serializer_class = Sessions
    queryset = Session.objects.all()
    
    
class SessionByWeekdayAPIView(generics.ListAPIView):
    serializer_class = SessionByWeekday
    
    def get_queryset(self):
        weekday = self.kwargs['weekday']
        
        return Session.objects.filter(weekday=weekday)
    

class ProfileAPIView(ObjectMultipleModelAPIView):
    username = self.request.user
    client = Client.objects.filter(username=username)
    bookings = Booking.objects.filter(client=client)
        
        
    querylist = [
        {'queryset': client, 'serializer_class': ClientSerializer},
        {'queryset': bookings, 'serializer_class': BookingSerializer},
    ]