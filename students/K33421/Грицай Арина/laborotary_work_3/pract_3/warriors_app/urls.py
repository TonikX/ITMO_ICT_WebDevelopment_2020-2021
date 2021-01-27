from django.urls import path
from .views import *

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('profession/', ProfessionAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),

    # задание 1
    path('skill/', SkillAPIView.as_view()),
    path('skill/create/', SkillCreateView.as_view()),

    # задание 2

    path('warriors/list_p/', WarriorsProfessionsAPIView.as_view()),
    path('warriors/list_sk/', WarriorsSkillsAllAPIView.as_view()),
    path('warriors/<int:pk>/info/', WarriorProfessionSkillAPIView.as_view()),
    path('warriors/<int:pk>/delete/', WarriorDeleteAPIView.as_view()),
    path('warriors/<int:pk>/update/', WarriorUpdateAPIView.as_view()),
]
