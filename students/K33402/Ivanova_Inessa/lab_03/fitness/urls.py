from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('lessons/', LessonsAPIView.as_view()),
    path('coaches/', CoachesAPIView.as_view()),
    path('timetable/', SessionsAPIView.as_view()),
    path('timetable/<str:weekday>', SessionByWeekdayAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),
    
]