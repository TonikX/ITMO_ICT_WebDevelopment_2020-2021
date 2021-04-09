from django.contrib import admin
from django.urls import path, include
from .views import index, ConferenceView, ConferenceDetailView


urlpatterns = [
    path('', index, name='index'),
    path('conferences/', ConferenceView.as_view(), name='conferences'),
    path('conferences/<slug:pk>/', ConferenceDetailView.as_view(), name='confernce_detail'),
]
