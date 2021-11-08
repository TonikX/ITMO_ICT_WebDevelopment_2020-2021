from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from main.serializers import BookReplicaSerializer, BookSerializer, LibrarianSerializer, LibraryHallSerializer, ReaderSerializer
from main.models import Book, BookReplica, CustomUser, Librarian, LibraryHall, Reader
from rest_framework import generics
from django.shortcuts import render


# Create your views here.
class LibraryHallListView(generics.ListCreateAPIView):
    queryset = LibraryHall.objects.all()
    serializer_class = LibraryHallSerializer


class LibraryHallDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibraryHall.objects.all()
    serializer_class = LibraryHallSerializer

    def delete(self, request, pk): # можно убрать
        print('LibraryHallView -> DELETE')
        try:
            library_hall = LibraryHall.objects.get(pk=pk)
            library_hall.readers.clear()
            library_hall.delete()
        except LibraryHall.DoesNotExist:
            return Response({'error': 'Object does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Deleted!'}, status=status.HTTP_202_ACCEPTED)


class LibraryHallReadersView(APIView):
    def get(self, request, pk, format=None):
        try:
            currentHall = LibraryHall.objects.get(pk=pk)
            readers = currentHall.readers.all()
            serializer = ReaderSerializer(readers, many=True)
        except LibraryHall.DoesNotExist:
            return Response({'error': 'Object does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LibraryHallCopiesView(APIView):
     def get(self, request, pk, format=None):
        try:
            currentHall = LibraryHall.objects.get(pk=pk)
            copies = currentHall.hall_copies.all()
            serializer = BookReplicaSerializer(copies, many=True)
        except LibraryHall.DoesNotExist:
            return Response({'error': 'Object does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCopiesView(APIView):
    def get(self, request, pk ,format=None):
        try:
            currentBook = Book.objects.get(pk=pk)
            copies = currentBook.book_copies.all()
            serializer = BookReplicaSerializer(copies, many=True)
        except Book.DoesNotExist:
            return Response({'error': 'Object does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ReaderListView(generics.ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class ReaderDetailView(generics.RetrieveUpdateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class ReaderByUserView(APIView):
    def get(self, request, pk ,format=None):
        try:
            currentUser = CustomUser.objects.get(pk=pk)
            readerProfile = currentUser.reader_profile
            serializer = ReaderSerializer(readerProfile)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Object does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LibrarianByUserView(APIView):
    def get(self, request, pk ,format=None):
        try:
            currentUser = CustomUser.objects.get(pk=pk)
            readerProfile = currentUser.librarian_profile
            serializer = LibrarianSerializer(readerProfile)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Object does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ReaderCopiesView(APIView):
     def get(self, request, pk ,format=None):
        try:
            currentReader = Reader.objects.get(pk=pk)
            copies = currentReader.reading_books.all()
            serializer = BookReplicaSerializer(copies, many=True)
        except Book.DoesNotExist:
            return Response({'error': 'Object does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LibrarianListView(generics.ListAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer


class ReplicaListView(generics.ListCreateAPIView):
    queryset = BookReplica.objects.all()
    serializer_class = BookReplicaSerializer


class ReplicaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookReplica.objects.all()
    serializer_class = BookReplicaSerializer
