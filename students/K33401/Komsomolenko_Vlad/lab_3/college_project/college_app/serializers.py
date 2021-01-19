from rest_framework import serializers
from .models import *


class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=userProfile
        fields='__all__'


class DisciplineSerializer(serializers.ModelSerializer):
  class Meta:
     model = Discipline
     fields = "__all__"

class MarkSerializer(serializers.ModelSerializer):
  class Meta:
     model = Mark
     fields = "__all__"

class PairSerializer(serializers.ModelSerializer):
  class Meta:
     model = Pair
     fields = "__all__"

class ScheduleSerializer(serializers.ModelSerializer):
  class Meta:
     model = Schedule
     fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
     model = Teacher
     fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
     model = Student
     fields = "__all__"

class TeacherDisciplineNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplineOfTeacher
        fields = "__all__"

class PairScheduleNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PairOfSchedule
        fields = "__all__"

class StudentMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkOfStudent
        fields = "__all__"

