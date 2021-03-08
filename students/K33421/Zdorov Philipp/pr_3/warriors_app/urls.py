from django.urls import path
from .views import *

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('warriors/<int:pk>', SingleWarriorAPIView.as_view()),
    path('warriors/<int:pk>/delete', DeleteWarriorAPIView.as_view()),
    path('warriors/<int:pk>/edit', EditWarriorAPIView.as_view()),
    path('warriors/<int:pk>/edit_skill', EditWarriorSkillAPIView.as_view()),
    path('skills/', SkillAPIView.as_view()),
    path('prof_warriors/', WarriorProfessionListAPIView.as_view()),
    path('skill_warriors/', WarriorSkillListAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('skill/create/', SkillCreateView.as_view()),
]
