from .serializers import *
from rest_framework import generics
from django.shortcuts import render

# Create your views here.

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ChickenListAPIView(generics.ListAPIView):
    serializer_class = ChickenRelatedSerializer
    queryset = Chicken.objects.all()


class ChickenInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chicken.objects.all()
    serializer_class = ChickenRelatedSerializer


class ChickenCreateAPIView(generics.CreateAPIView):
    serializer_class = ChickenSerializer
    queryset = Chicken.objects.all()


class BreedListAPIView(generics.ListAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class BreedInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedCreateAPIView(generics.CreateAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceRelatedSerializer
    queryset = Service.objects.all()


class ServiceInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceCreateAPIView(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class CellListAPIView(generics.ListAPIView):
    serializer_class = CellSerializer
    queryset = Cell.objects.all()


class CellInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer


class CellCreateAPIView(generics.CreateAPIView):
    serializer_class = CellSerializer
    queryset = Cell.objects.all()


class ServiceNestedAPIView(generics.ListAPIView):
    serializer_class = ServiceNestedSerializer
    queryset = Service.objects.all()


class ChickenNestedAPIView(generics.ListAPIView):
    serializer_class = ChickenNestedSerializer
    queryset = Chicken.objects.all()