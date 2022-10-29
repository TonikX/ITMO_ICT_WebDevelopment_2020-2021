
from django.urls import path
from .views import *

app_name = 'warriors'

urlpatterns = [
  path('warriors/', WarriorAPIView.as_view()),
  path('warriors/create', WarriorCreateAPIView.as_view()),
  path('warriors/delete/<int:pk>', WarriorDestroyView.as_view()),
  path('warriors/update/<int:pk>', WarriorUpdateView.as_view()),
]