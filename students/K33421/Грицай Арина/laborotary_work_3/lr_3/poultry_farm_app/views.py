from .serializers import *
from rest_framework import generics
from rest_framework import permissions


class UserListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAddAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ChickenListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChickenRelatedSerializer
    queryset = Chicken.objects.all()


class ChickenChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Chicken.objects.all()
    serializer_class = ChickenRelatedSerializer


class ChickenAddAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChickenSerializer
    queryset = Chicken.objects.all()


class BreedListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class BreedChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedAddAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class ServiceListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ServiceRelatedSerializer
    queryset = Service.objects.all()


class ServiceChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceAddAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class CellListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CellSerializer
    queryset = Cell.objects.all()


class CellChangeInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cell.objects.all()
    serializer_class = CellSerializer


class CellAddAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CellSerializer
    queryset = Cell.objects.all()


class ServiceNestedAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ServiceNestedSerializer
    queryset = Service.objects.all()


class ChickenNestedAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChickenNestedSerializer
    queryset = Chicken.objects.all()
