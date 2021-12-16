from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', WarriorCreateAPIView.as_view()),
   path('warriors/list/', WarriorListAPIView.as_view()),
   path('warriors/delete/<int:pk>', WarriorDestroyView.as_view()),
   path('warriors/<int:pk>', SingleWarriorAPIView.as_view()),
   path('warriors/update/<int:pk>', WarriorUpdateView.as_view()),
   path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
   path('skill/create/', SkillsCreateView.as_view()),
]