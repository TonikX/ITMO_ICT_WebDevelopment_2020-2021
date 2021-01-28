from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from hotel_app.models import *
from hotel_app.serializers import *


# Create your views here.
class RoomAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class EmployeeAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class ResidentAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ResidentSerializer
    queryset = Resident.objects.all()


class BookingRecordAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingRecordSerializer
    queryset = BookingRecord.objects.all()


class CleaningScheduleAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CleaningScheduleSerializer
    queryset = CleaningSchedule.objects.all()