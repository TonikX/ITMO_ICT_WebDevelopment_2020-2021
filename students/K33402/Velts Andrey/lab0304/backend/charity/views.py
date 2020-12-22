from rest_framework import viewsets
from .serializers import CharitySerializer
from .models import Charity


class PetsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CharitySerializer
    queryset = Charity.objects.all()
    permission_classes = []
