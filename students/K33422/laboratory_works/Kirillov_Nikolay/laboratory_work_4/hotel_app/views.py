from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class RoomAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    lookup_field = 'pk'


class RoomAddAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class StaffAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class StaffChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    lookup_field = 'pk'


class StaffAddAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class GuestAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()


class GuestChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()
    lookup_field = 'pk'


class GuestAddAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()


class CleaningAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()


class CleaningChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()
    lookup_field = 'pk'


class CleaningAddAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()


class UserChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'pk'


class UserAddAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
