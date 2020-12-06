from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import LostSerializer
from .models import Lost


class LostViewSet(viewsets.ModelViewSet):
    serializer_class = LostSerializer
    queryset = Lost.objects.all()
    permission_classes = []
    parser_class = (MultiPartParser, FormParser)
