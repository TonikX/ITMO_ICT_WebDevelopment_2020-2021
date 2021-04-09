from django.urls import path
from .views import *


app_name = "warriors"


urlpatterns = [
   path('skill/', SkillAPIView.as_view()),
   path('skill/create/', SkillCreateView.as_view()),
   path('profession/create/', ProfessionCreateAPIView.as_view()),
   path('skill_of_warrior/create/', SkillOfWarriorCreateAPIView.as_view()),

   path('warrior/', WarriorListAPIView.as_view()),
   path('warrior/skill/', WarriorsSkillView.as_view()),
   path('warrior/prof/', WarriorsProfessionSkillView.as_view()),
   path('warrior/create/', WarriorCreateAPIView.as_view()),
   path('warrior/<int:pk>', WarriorAllView.as_view()),

]
