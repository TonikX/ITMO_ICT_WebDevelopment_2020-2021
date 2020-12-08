from django.urls import path
from .views import *

urlpatterns = [
    path('creations/', CreationListAPIView.as_view()),
    path('creations/create/', CreationCreateAPIView.as_view()),
    path('creations/<int:pk>/', CreationRetrieveAPIView.as_view()),
    path('creations/<int:pk>/update/', CreationUpdateAPIView.as_view()),
    path('creations/<int:pk>/delete/', CreationDeleteAPIView.as_view()),
    path('authors/', AuthorListAPIView.as_view()),
    path('authors/create/', AuthorCreateAPIView.as_view()),
    path('authors/<int:pk>/', AuthorRetrieveAPIView.as_view()),
    path('authors/<int:pk>/update/', AuthorUpdateAPIView.as_view()),
    path('authors/<int:pk>/delete/', AuthorDeleteAPIView.as_view()),
    path('reviews/', ReviewListAPIView.as_view()),
    path('reviews/create/', ReviewCreateAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewRetrieveAPIView.as_view()),
    path('reviews/<int:pk>/update/', ReviewUpdateAPIView.as_view()),
    path('reviews/<int:pk>/delete/', ReviewDeleteAPIView.as_view()),
]