from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

#
# from knox.views import LoginView as KnoxLoginView
# from rest_framework.authentication import BasicAuthentication
#
# class LoginView(KnoxLoginView):
#     authentication_classes = [BasicAuthentication]



class AirlineViewSet(viewsets.ModelViewSet):
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = AirlineSerializer

    def get_queryset(self):
        return self.request.user.airlines.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CitySerializer

