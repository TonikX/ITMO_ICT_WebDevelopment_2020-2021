# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from polls_app.serializers import *


class IsPollCreator(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user == Poll.objects.get(pk=view.kwargs['pk']).creator


class PollsAPIView(ListAPIView):

    permission_classes = [permissions.AllowAny]

    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class PollCreateAPIView(CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PollCreateSerializer
    queryset = Poll.objects.all()


class PollAPIView(RetrieveAPIView):

    permission_classes = [permissions.AllowAny]

    serializer_class = PollDetailsSerializer
    queryset = Poll.objects.all()


class PollUpdateAPIView(UpdateAPIView):

    permission_classes = [IsPollCreator]

    serializer_class = PollCreateSerializer
    queryset = Poll.objects.all()


class PollDeleteAPIView(DestroyAPIView):

    permission_classes = [IsPollCreator]

    serializer_class = PollSerializer
    queryset = Poll.objects.all()
