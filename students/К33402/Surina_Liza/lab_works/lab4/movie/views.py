from rest_framework import generics
from rest_framework import viewsets, permissions
from .serializers import MovieSerializer, ReviewCreateSerializer, UserSerializer, MovieDetailSerializer
from .models import Movie

from django.core.exceptions import PermissionDenied


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieDetailView(generics.RetrieveAPIView):
    """Вывод фильма"""

    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer


class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва к фильму"""
    permission_classes = [permissions.AllowAny]
    serializer_class = ReviewCreateSerializer
