from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('warriors/with_prof', WarriorWithProfAPIView.as_view()),
    path('warriors/with_skills', WarriorWithSkillsAPIView.as_view()),
    path('warrior/create/', WarriorCreateAPIView.as_view()),
    path('warrior/action/<int:pk>', WarriorActionAPIView.as_view()),
    path('professions/', ProfessionAPIView.as_view()),
    path('profession/create/', ProfessionCreateAPIView.as_view()),
    path('skills/', SkillAPIView.as_view()),
    path('skill/create/', SkillCreateAPIView.as_view()),
    path('skillOfWarrior/', SkillOfWarriorAPIView.as_view()),
    path('skillOfWarrior/create/', SkillOfWarriorCreateAPIView.as_view()),
]
