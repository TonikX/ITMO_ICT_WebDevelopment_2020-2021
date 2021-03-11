from main.views import BookCopiesView, BookListView, LibrarianByUserView, LibrarianListView, LibraryHallDetailView, LibraryHallListView, LibraryHallReadersView, ReaderByUserView, ReaderCopiesView, ReaderDetailView, ReaderListView, ReplicaDetailView, ReplicaListView, BookDetailView, LibraryHallCopiesView
from main.models import LibraryHall
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('library_halls/', LibraryHallListView.as_view()),
    path('library_hall/<int:pk>/', LibraryHallDetailView.as_view()),
    path('library_hall/<int:pk>/readers/', LibraryHallReadersView.as_view()),
    path('library_hall/<int:pk>/copies/', LibraryHallCopiesView.as_view()),
    path('books/', BookListView.as_view()),
    path('book/<int:pk>/', BookDetailView.as_view()),
    path('book/<int:pk>/copies/', BookCopiesView.as_view()),
    path('readers/', ReaderListView.as_view()),
    path('reader/<int:pk>/', ReaderDetailView.as_view()),
    path('reader/<int:pk>/copies/', ReaderCopiesView.as_view()),
    path('reader_by_user/<int:pk>/', ReaderByUserView.as_view()),
    path('librarians/', LibrarianListView.as_view()),
    path('librarian_by_user/<int:pk>/', LibrarianByUserView.as_view()),
    path('copies/', ReplicaListView.as_view()),
    path('copy/<int:pk>/', ReplicaDetailView.as_view())
]