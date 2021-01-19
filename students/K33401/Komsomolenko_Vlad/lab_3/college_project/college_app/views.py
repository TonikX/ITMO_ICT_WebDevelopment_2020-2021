from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import *
import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class DisciplineCreateAPIView(generics.CreateAPIView):
   serializer_class = DisciplineSerializer
   queryset = Discipline.objects.all()
   permission_classes = [IsAuthenticated]

class DisciplineAPIView(generics.ListAPIView):
   serializer_class = DisciplineSerializer
   queryset = Discipline.objects.all()
   permission_classes = [IsAuthenticated]

class PairCreateAPIView(generics.CreateAPIView):
   serializer_class = PairSerializer
   queryset = Pair.objects.all()
   permission_classes = [IsAuthenticated]

class PairAPIView(generics.ListAPIView):
   serializer_class = PairSerializer
   queryset = Pair.objects.all()
   permission_classes = [IsAuthenticated]

class TeacherCreateAPIView(generics.CreateAPIView):
   serializer_class = TeacherSerializer
   queryset = Teacher.objects.all()
   permission_classes = [IsAuthenticated]

class TeacherAPIView(generics.ListAPIView):
   serializer_class = TeacherSerializer
   queryset = Teacher.objects.all()
   permission_classes = [IsAuthenticated]

class TeacherDisciplineView(generics.CreateAPIView):
   serializer_class = TeacherDisciplineNestedSerializer
   queryset = DisciplineOfTeacher.objects.all()
   permission_classes = [IsAuthenticated]

class StudentCreateAPIView(generics.CreateAPIView):
   serializer_class = StudentSerializer
   queryset = Student.objects.all()
   permission_classes = [IsAuthenticated]

class StudentAPIView(generics.ListAPIView):
   serializer_class = StudentSerializer
   queryset = Student.objects.all()
   permission_classes = [IsAuthenticated]

class PairCreateAPIView(generics.CreateAPIView):
   serializer_class = PairSerializer
   queryset = Pair.objects.all()
   permission_classes = [IsAuthenticated]

class PairAPIView(generics.ListAPIView):
   serializer_class = PairSerializer
   queryset = Pair.objects.all()
   permission_classes = [IsAuthenticated]

class ScheduleCreateAPIView(generics.CreateAPIView):
   serializer_class = ScheduleSerializer
   queryset = Schedule.objects.all()
   permission_classes = [IsAuthenticated]

class ScheduleAPIView(generics.ListAPIView):
   serializer_class = ScheduleSerializer
   queryset = Schedule.objects.all()
   permission_classes = [IsAuthenticated]

class PairScheduleView(generics.CreateAPIView):
   serializer_class = PairScheduleNestedSerializer
   queryset = PairOfSchedule.objects.all()
   permission_classes = [IsAuthenticated]

class MarkCreateAPIView(generics.CreateAPIView):
   serializer_class = MarkSerializer
   queryset = Mark.objects.all()
   permission_classes = [IsAuthenticated]

class MarkAPIView(generics.ListAPIView):
   serializer_class = MarkSerializer
   queryset = Mark.objects.all()
   permission_classes = [IsAuthenticated]

class StudentMarkAPIView(generics.CreateAPIView):
   serializer_class = StudentMarkSerializer
   queryset = MarkOfStudent.objects.all()
   permission_classes = [IsAuthenticated]

class StudentMarkUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = StudentMarkSerializer
   queryset = MarkOfStudent.objects.all()
   permission_classes = [IsAuthenticated]

class MarkUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = MarkSerializer
   queryset = Mark.objects.all()
   permission_classes = [IsAuthenticated]

class StudentUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = StudentSerializer
   queryset = Student.objects.all()
   permission_classes = [IsAuthenticated]

class ScheduleUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = ScheduleSerializer
   queryset = Schedule.objects.all()
   permission_classes = [IsAuthenticated]

class TeacherUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = TeacherSerializer
   queryset = Teacher.objects.all()
   permission_classes = [IsAuthenticated]


class UserProfileListCreateView(generics.ListCreateAPIView):
   queryset = userProfile.objects.all()
   serializer_class = userProfileSerializer
   permission_classes = [IsAuthenticated]

   def perform_create(self, serializer):
      user = self.request.user
      serializer.save(user=user)

