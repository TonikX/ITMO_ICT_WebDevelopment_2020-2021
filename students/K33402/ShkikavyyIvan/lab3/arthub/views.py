from django.shortcuts import render
from rest_framework import authentication, permissions

from .serializers import *
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.response import Response


class IsReviewer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user == Review.objects.get(pk=view.kwargs['pk']).author


class IsRedactorAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(request.user.is_superuser)


class CreationListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreationFullSerializer
    queryset = Creation.objects.all()


class CreationCreateAPIView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CreationSerializer
    queryset = Creation.objects.all()


class CreationRetrieveAPIView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreationFullSerializer
    queryset = Creation.objects.all()


class CreationUpdateAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CreationSerializer
    queryset = Creation.objects.all()


class CreationDeleteAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CreationSerializer
    queryset = Creation.objects.all()


class AuthorListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorCreateAPIView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorRetrieveAPIView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorUpdateAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorDeleteAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class ReviewListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewFullSerializer

    def get_queryset(self):
        return Review.objects.filter(author=self.request.user)


class CreationListAuthorAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreationSerializer
    queryset = Creation.objects.all()

    def get_queryset(self):
        return Creation.objects.filter(creator=self.kwargs["authorId"])


class ReviewListCreationAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get_queryset(self):
        return Review.objects.filter(creation=self.kwargs["creationId"])


class ReviewCreateAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ReviewRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsReviewer]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ReviewUpdateAPIView(UpdateAPIView):
    permission_classes = [IsReviewer]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ReviewDeleteAPIView(DestroyAPIView):
    permission_classes = [IsReviewer]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
