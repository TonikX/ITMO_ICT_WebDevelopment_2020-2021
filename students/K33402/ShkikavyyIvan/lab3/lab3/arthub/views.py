from django.shortcuts import render
from rest_framework import authentication, permissions

from .serializers import *
from rest_framework.generics import *


class IsReviewer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user == Review.objects.get(pk=view.kwargs['pk']).author


class CreationListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreationSerializer
    queryset = Creation.objects.all()


class CreationCreateAPIView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CreationSerializer
    queryset = Creation.objects.all()


class CreationRetrieveAPIView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreationSerializer
    queryset = Creation.objects.all()
    lookup_field = 'pk'


class CreationUpdateAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CreationSerializer
    queryset = Creation.objects.all()
    lookup_field = 'pk'


class CreationDeleteAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CreationSerializer
    queryset = Creation.objects.all()
    lookup_field = 'pk'


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
    lookup_field = 'pk'


class AuthorUpdateAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    lookup_field = 'pk'


class AuthorDeleteAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    lookup_field = 'pk'


class ReviewListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewFullSerializer

    def get_queryset(self):
        ###print(Review.objects.filter(author=self.request.user).all())
        return Review.objects.filter(author=self.request.user)


class ReviewCreateAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ReviewRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsReviewer]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    lookup_field = 'pk'


class ReviewUpdateAPIView(UpdateAPIView):
    permission_classes = [IsReviewer]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    lookup_field = 'pk'


class ReviewDeleteAPIView(DestroyAPIView):
    permission_classes = [IsReviewer]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    lookup_field = 'pk'
