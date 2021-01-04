from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = {
        permissions.AllowAny
    }
    serializer_class = TodoSeriallizer
