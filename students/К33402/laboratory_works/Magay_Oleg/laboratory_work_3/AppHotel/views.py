from rest_framework.generics import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class RoomListView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class RoomAllView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class RoomCreateView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class GuestListView(ListAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsAuthenticated]


class GuestAllView(RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsAuthenticated]

class GuestCreateView(CreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsAuthenticated]


class StaffListView(ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]


class StaffAllView(RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]


class StaffCreateView(CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]


class StaffCleaningListView(ListAPIView):
    queryset = StaffCleaning.objects.all()
    serializer_class = StaffCleaningSerializer
    permission_classes = [IsAuthenticated]


class StaffCleaningAllView(RetrieveUpdateDestroyAPIView):
    queryset = StaffCleaning.objects.all()
    serializer_class = StaffCleaningSerializer
    permission_classes = [IsAuthenticated]


class StaffCleaningCreateView(CreateAPIView):
    queryset = StaffCleaning.objects.all()
    serializer_class = StaffCleaningSerializer
    permission_classes = [IsAuthenticated]


class CleaningParamsListView(ListAPIView):
    queryset = CleaningParams.objects.all()
    serializer_class = CleaningParamsSerializer
    permission_classes = [IsAuthenticated]


class CleaningParamsAllView(RetrieveUpdateDestroyAPIView):
    queryset = CleaningParams.objects.all()
    serializer_class = CleaningParamsSerializer
    permission_classes = [IsAuthenticated]


class CleaningParamsCreateView(CreateAPIView):
    queryset = CleaningParams.objects.all()
    serializer_class = CleaningParamsSerializer
    permission_classes = [IsAuthenticated]
