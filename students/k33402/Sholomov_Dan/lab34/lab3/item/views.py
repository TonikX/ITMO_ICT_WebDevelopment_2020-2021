from rest_framework import viewsets
from .serializers import ItemsSerializer
from .models import Item


class ItemsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ItemsSerializer
    queryset = Item.objects.all()
    permission_classes = []
