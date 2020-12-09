from django.db.models import Q
from rest_framework import generics
from .serializers import *


# users info

class StudentsListAPIView(generics.ListAPIView):

    serializer_class = StudentSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        queryset = self.model.objects.filter(role='s')
        return queryset


class TeachersListAPIView(generics.ListAPIView):

    serializer_class = TeacherSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        queryset = self.model.objects.filter(role='t')
        return queryset


class StaffListAPIView(generics.ListAPIView):

    serializer_class = UserSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        queryset = self.model.objects.filter(Q(role='a') | Q(role='d'))
        return queryset


# student groups

class StudentGroupsListAPIView(generics.ListAPIView):

    serializer_class = StudentGroupSerializer
    queryset = StudentGroup.objects.all()


class StudentGroupCreateAPIView(generics.CreateAPIView):

    serializer_class = StudentGroupCreateSerializer
    queryset = StudentGroup.objects.all()


class StudentGroupPageAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = StudentGroupSerializer
    queryset = StudentGroup.objects.all()
    lookup_field = 'group_number'


# schedule

class ScheduleListAPIView(generics.ListAPIView):

    serializer_class = ScheduleSerializer
    queryset = ScheduleEntry.objects.all()


class ScheduleEntryCreateAPIView(generics.CreateAPIView):

    serializer_class = ScheduleCreateSerializer
    queryset = ScheduleEntry.objects.all()


class ScheduleEntryPageAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ScheduleSerializer
    queryset = ScheduleEntry.objects.all()


class MyScheduleListAPIView(generics.ListAPIView):

    serializer_class = ScheduleSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        if self.request.user.role == 's':
            student_group = self.request.user.student_group
            queryset = self.model.objects.filter(group_number=student_group)
            return queryset
        elif self.request.user.role == 't':
            teacher = self.request.user
            queryset = self.model.objects.filter(teacher=teacher)
            return queryset
        else:
            return None


# subjects

class SubjectsListAPIView(generics.ListAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SubjectCreateAPIView(generics.CreateAPIView):

    serializer_class = SubjectCreateSerializer
    queryset = Subject.objects.all()


class SubjectPageAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


# rooms

class RoomsListAPIView(generics.ListAPIView):

    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomCreateAPIView(generics.CreateAPIView):

    serializer_class = RoomCreateSerializer
    queryset = Room.objects.all()


class RoomPageAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    lookup_field = 'room_number'


# teachings

class TeachingsListAPIView(generics.ListAPIView):

    serializer_class = TeachingSerializer
    queryset = Teaching.objects.all()


class TeachingCreateAPIView(generics.CreateAPIView):

    serializer_class = TeachingCreateSerializer
    queryset = Teaching.objects.all()


class TeachingPageAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TeachingSerializer
    queryset = Teaching.objects.all()


# semester grades

class SemesterGradesListAPIView(generics.ListAPIView):

    serializer_class = SemesterGradeSerializer
    queryset = SemesterGrade.objects.all()


class SemesterGradeCreateAPIView(generics.CreateAPIView):

    serializer_class = SemesterGradeCreateSerializer
    queryset = SemesterGrade.objects.all()


class SemesterGradePageAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = SemesterGradeSerializer
    queryset = SemesterGrade.objects.all()
