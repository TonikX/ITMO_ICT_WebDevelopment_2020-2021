from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

urlpatterns = [
    path('disciplines/', DisciplineAPIView.as_view()),
    path('discipline/create/', DisciplineCreateAPIView.as_view()),
    path('pairs/', PairAPIView.as_view()),
    path('pair/create/', PairCreateAPIView.as_view()),
    path('teachers/', TeacherAPIView.as_view()),
    path('teacher/create/', TeacherCreateAPIView.as_view()),
    path('teacher/updel/<int:pk>', TeacherUpdateDeleteView.as_view()),
    path('teacher/adddisc/', TeacherDisciplineView.as_view()),
    path('students/', StudentAPIView.as_view()),
    path('student/create/', StudentCreateAPIView.as_view()),
    path('student/updel/<int:pk>', StudentUpdateDeleteView.as_view()),
    path('student/addmark/', StudentMarkAPIView.as_view()),
    path('pairs/', PairAPIView.as_view()),
    path('pair/create/', PairCreateAPIView.as_view()),
    path('schedules/', ScheduleAPIView.as_view()),
    path('schedule/create/', ScheduleCreateAPIView.as_view()),
    path('schedule/addpairs/', PairScheduleView.as_view()),
    path('marks/', MarkAPIView.as_view()),
    path('mark/create/', MarkCreateAPIView.as_view()),
    path('mark/updel/<int:pk>', StudentMarkUpdateDeleteView.as_view()),
    path('mark/updel/<int:pk>', StudentMarkUpdateDeleteView.as_view()),
]