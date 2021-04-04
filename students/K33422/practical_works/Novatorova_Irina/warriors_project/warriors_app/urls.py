from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('warrior/', WarriorAPIView.as_view()),
   path('prof/create/', ProfessionCreateView.as_view()),
   path('skill/', SkillAPIView.as_view()),
   path('skill/create/', SkillCreateView.as_view()),
   path('war_list/prof/', WarriorProfView.as_view()),
   path('war_list/skill/', WarriorSkillView.as_view()),
   path('warrior/<int:pk>/', WarriorInfoView.as_view()),
   path('warrior/<int:pk>/edit/', WarriorEditView.as_view()),
   path('warrior/<int:pk>/delete/', WarriorDeleteView.as_view()),
]
