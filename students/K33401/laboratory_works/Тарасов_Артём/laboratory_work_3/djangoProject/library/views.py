from rest_framework import viewsets
from rest_framework.generics import *
from rest_framework.mixins import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class BookView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    model = Book

    def list(self, request):
        queryset = self.model.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.model.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def create(self, request):
        model_obj = request.data.copy()
        model_obj['owner'] = request.user.id
        serializer = self.serializer_class(data=model_obj)
        serializer.is_valid(raise_exception=True)
        model_obj_saved = serializer.save()
        return Response({"success": "Object '{}' created successfully".format(model_obj_saved)})

    def update(self, request, pk=None):
        model_obj = get_object_or_404(self.model.objects.all(), pk=pk)
        if model_obj.owner != request.user.id:
            return Response("Access denied")
        data = request.data.copy()
        serializer = self.serializer_class(instance=model_obj, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        model_obj_saved = serializer.save()
        return Response({
            "success": "Object '{}' updated successfully".format(model_obj_saved)
        })

    def destroy(self, request, pk=None):
        model_obj = get_object_or_404(self.model.objects.all(), pk=pk)
        if model_obj.owner != request.user.id:
            return Response("Access denied")
        model_obj.delete()
        return Response({
            "success": "Object deleted successfully"
        })


class ReaderView(BookView):
    serializer_class = ReaderSerializer
    model = Reader


class IssuingAInstanceView(BookView):
    serializer_class = IssuingAInstanceSerializer
    model = IssuingAInstance


class InstanceOfBookView(BookView):
    serializer_class = InstanceOfBookSerializer
    model = InstanceOfBook


class ReadingRoomView(BookView):
    serializer_class = ReadingRoomSerializer
    model = ReadingRoom


class InstanceOfBookInReadingRoomView(BookView):
    serializer_class = InstanceOfBookInReadingRoomSerializer
    model = InstanceOfBookInReadingRoom


class RegistersView(BookView):
    serializer_class = RegistersSerializer
    model = Registers
