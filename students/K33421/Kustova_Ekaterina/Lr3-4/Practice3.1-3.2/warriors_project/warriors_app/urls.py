from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', WarriorAPIView.as_view()),
   path('profession/create/', ProfessionCreateView.as_view()),
   path('skills/', SkillGetAPIView.as_view()),
   path('skills/create/', SkillCreateAPIView.as_view()),

   path('warriors_skills/', WarriorsSkills.as_view()),
   path('warriors_professions/', WarriorsProfession.as_view()),
   path('warriors/<int:pk>/', OneWarriorAPIView.as_view()),
   path('warriors/<int:pk>/edit/', OneWarriorEditAPIView.as_view()),
   path('warriors/<int:pk>/delete/', OneWarriorDestroyAPIView.as_view()),
]


