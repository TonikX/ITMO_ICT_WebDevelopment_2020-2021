# Create your views here.
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from polls_app.serializers import *


class IsPollCreator(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user == Poll.objects.get(pk=view.kwargs['pk']).creator


class PollsAPIView(ListAPIView):

    permission_classes = [permissions.AllowAny]

    serializer_class = PollSerializer
    queryset = Poll.objects.all()

    def get_queryset(self):
        queryset = Poll.objects.all()
        current = self.request.query_params.get('current')
        user = self.request.user

        if current:
            queryset = queryset.filter(creator=user)

        return queryset


class PollCreateAPIView(CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PollCreateSerializer
    queryset = Poll.objects.all()


class PollAPIView(RetrieveAPIView):

    permission_classes = [permissions.AllowAny]

    serializer_class = PollDetailsSerializer
    queryset = Poll.objects.all()


class StatisticAPIView(ListAPIView):

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UserToAnswerSerializer
    queryset = UserToAnswer.objects.all()

    def get_queryset(self):
        queryset = UserToAnswer.objects.all()
        answer = self.request.query_params.get('answer')

        if answer:
            queryset = queryset.filter(answer_id=answer)

        return queryset


class PollUpdateAPIView(UpdateAPIView):

    permission_classes = [IsPollCreator]

    serializer_class = PollCreateSerializer
    queryset = Poll.objects.all()


class PollDeleteAPIView(DestroyAPIView):

    permission_classes = [IsPollCreator]

    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class UserToAnswerCreateAPIView(CreateAPIView):

    serializer_class = UserToAnswerSerializer
    queryset = UserToAnswer.objects.all()
