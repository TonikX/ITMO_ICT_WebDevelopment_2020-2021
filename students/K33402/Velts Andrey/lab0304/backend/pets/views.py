from rest_framework import viewsets
from .serializers import PetsSerializer
from .models import Pet


class PetsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PetsSerializer
    queryset = Pet.objects.all()
    permission_classes = []
