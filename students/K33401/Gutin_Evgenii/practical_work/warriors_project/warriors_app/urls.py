from django.urls import path
from .views import *

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('skills/create/', CreateSkills.as_view(), name="create skills"),
    path('skills/', GetSkills.as_view(), name="get skills"),
    path('skill_of_warrior/create/', SkillOfWarriorCreateAPIView.as_view()),
    path('warriors/list/', WarriorListAPIView.as_view()),
    path('warriors_with_jobs/list/', WarriorWithJobsAPIView.as_view()),
    path('warriors_with_skills/list/', WarriorWithSkillsAPIView.as_view()),
    path('warriors/create/', WarriorCreateAPIView.as_view()),
    path('warriors/<int:pk>/', WarriorSingleAPIView.as_view()),
    path('warriors/<int:pk>/update/', WarriorUpdateAPIView.as_view()),
    path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
]
