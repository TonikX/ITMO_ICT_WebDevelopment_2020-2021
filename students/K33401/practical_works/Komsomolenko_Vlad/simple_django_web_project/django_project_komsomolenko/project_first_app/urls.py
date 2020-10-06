from django.urls import path
from . import views

urlpatterns = [
    path('owners/', views.owner, name='owner'),
    path('owners/<int:pk>/', views.owner_id.as_view()),
]
