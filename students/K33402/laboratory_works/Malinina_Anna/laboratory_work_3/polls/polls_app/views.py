# Create your views here.
from rest_framework import viewsets

from polls_app.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'create':
            return AppUserCreateSerializer
        if hasattr(self, 'action') and self.action == 'retrieve':
            return UserDetailsSerializer
        if hasattr(self, 'action') and self.action == 'update':
            return AppUserUpdateSerializer
        return AppUserSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'create':
            return PollCreateSerializer
        if hasattr(self, 'action') and self.action == 'update':
            return PollCreateSerializer
        if hasattr(self, 'action') and self.action == 'retrieve':
            return PollDetailsSerializer
        return PollSerializer
