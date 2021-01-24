from .serializers import *
from rest_framework import generics


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAddAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ChickenListAPIView(generics.ListAPIView):
    serializer_class = ChickenRelatedSerializer
    queryset = Chicken.objects.all()


class ChickenChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chicken.objects.all()
    serializer_class = ChickenRelatedSerializer


class ChickenAddAPIView(generics.CreateAPIView):
    serializer_class = ChickenSerializer
    queryset = Chicken.objects.all()


class BreedListAPIView(generics.ListAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class BreedChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedAddAPIView(generics.CreateAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceRelatedSerializer
    queryset = Service.objects.all()


class ServiceChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceAddAPIView(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class CellListAPIView(generics.ListAPIView):
    serializer_class = CellSerializer
    queryset = Cell.objects.all()


class CellChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer


class CellAddAPIView(generics.CreateAPIView):
    serializer_class = CellSerializer
    queryset = Cell.objects.all()


class ServiceNestedAPIView(generics.ListAPIView):
    serializer_class = ServiceNestedSerializer
    queryset = Service.objects.all()


class ChickenNestedAPIView(generics.ListAPIView):
    serializer_class = ChickenNestedSerializer
    queryset = Chicken.objects.all()
