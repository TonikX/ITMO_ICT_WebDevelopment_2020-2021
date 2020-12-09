from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from drf_multiple_model.views import ObjectMultipleModelAPIView
import requests

class LessonTypeAPIView(generics.ListAPIView):
    serializer_class = LessonTypeSerializer
    queryset = LessonType.objects.all()
    
    
class CoachesAPIView(generics.ListAPIView):
    serializer_class = CoachSerializer
    queryset = Coach.objects.all()
    

class SessionsAPIView(generics.ListAPIView):
    serializer_class = SessionSerializer
    queryset = LessonSession.objects.all()
    
    
class SessionByWeekdayAPIView(generics.ListAPIView):
    serializer_class = SessionByWeekday
    
    def get_queryset(self):
        weekday = self.kwargs['weekday']
        
        return LessonSession.objects.filter(weekday=weekday)
    

class ProfileAPIView(generics.ListAPIView):
    serializer_class = ClientSerializer
    
    def get_queryset(self):
        username = self.request.user
        
        return Client.objects.filter(username=username)
        
        
class BookingCreateAPIView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
    def create(self, request, *args, **kwargs):
        session = LessonSession.objects.filter(id=self.kwargs['id'])[0]
        client = Client.objects.filter(username=self.request.user)[0]
        if Booking.objects.filter(session=session, client=client):
            return Response("Вы уже записаны на это занятие", status=403)
        else:
            book = Booking.objects.create(session=session, client=client)
            return Response("Вы успешно записались на занятие", status=200)
            
            
class BookingDeleteAPIView(generics.DestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
    def delete(self, request, *args, **kwargs):
        session = LessonSession.objects.filter(id=self.kwargs['id'])[0]
        client = Client.objects.filter(username=self.request.user)[0]
        booking = Booking.objects.filter(session=session, client=client)[0]
        booking.delete()
        return Response("Вы успешно отписались от занятия", status=200)
            
    