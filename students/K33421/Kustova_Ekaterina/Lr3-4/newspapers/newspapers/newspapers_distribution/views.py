from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import authentication, permissions


# Просмотр всех пользователей
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Создание нового пользователя
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Редактирование конкретного пользователя
class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


# Посмотр всех газет
class NewspaperAPIView(generics.ListAPIView):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer


# Редактирование конкретной газеты
class NewspaperUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer
    lookup_field = 'pk'


# Создание новой газеты
class NewspaperCreateAPIView(generics.CreateAPIView):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer


# Посмотр всех почтовых отделений
class PostOfficeAPIView(generics.ListAPIView):
    queryset = PostOffice.objects.all()
    serializer_class = PostOfficeSerializer


# Редактирование конкретного почтового отделения
class PostOfficeUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = PostOffice.objects.all()
    serializer_class = PostOfficeSerializer
    lookup_field = 'pk'


# Создание нового отделения
class PostOfficeCreateAPIView(generics.CreateAPIView):
    queryset = PostOffice.objects.all()
    serializer_class = PostOfficeSerializer


# Посмотр всех типографий
class PrinteryAPIView(generics.ListAPIView):
    queryset = Printery.objects.all()
    serializer_class = PrinterySerializer


# Редактирование конкретной типографии
class PrinteryUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Printery.objects.all()
    serializer_class = PrinterySerializer
    lookup_field = 'pk'


# Создание новой типографии
class PrinteryCreateAPIView(generics.CreateAPIView):
    queryset = Printery.objects.all()
    serializer_class = PrinterySerializer


# Посмотр всех печатей
class PrintAPIView(generics.ListAPIView):
    queryset = Print.objects.all()
    serializer_class = PrintSerializer


# Редактирование конкретной печати
class PrintUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Print.objects.all()
    serializer_class = PrintSerializer
    lookup_field = 'pk'


# Создание новой печати
class PrintCreateAPIView(generics.CreateAPIView):
    queryset = Print.objects.all()
    serializer_class = PrintSerializer


# Посмотр всех партий газет
class NewspapersPartyAPIView(generics.ListAPIView):
    queryset = NewspapersParty.objects.all()
    serializer_class = NewspapersPartySerializer


# Редактирование конкретной партии газет
class NewspapersPartyUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = NewspapersParty.objects.all()
    serializer_class = NewspapersPartySerializer
    lookup_field = 'pk'


# Создание новой партий газет
class NewspapersPartyCreateAPIView(generics.CreateAPIView):
    queryset = NewspapersParty.objects.all()
    serializer_class = NewspapersPartySerializer


# Посмотр всех отчётов
class DistributionReportAPIView(generics.ListAPIView):
    queryset = DistributionReport.objects.all()
    serializer_class = DistributionReportSerializer


# Редактирование конкретного отчёта
class DistributionReportUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = DistributionReport.objects.all()
    serializer_class = DistributionReportSerializer
    lookup_field = 'pk'


# Создание нового отчёта
class DistributionReportCreateAPIView(generics.CreateAPIView):
    queryset = DistributionReport.objects.all()
    serializer_class = DistributionReportSerializer
