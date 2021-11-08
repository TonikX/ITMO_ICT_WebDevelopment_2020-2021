from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('skills/', SkillAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('skill/create/', SkillCreateView.as_view()),
    path('warriors/list_p/', WarriorsProfessionsAPIView.as_view()),
    path('warriors/list_s/', WarriorsSkillsAPIView.as_view()),
    path('warriors/<int:pk>/info/', WarriorProfessionSkillAPIView.as_view()),
    path('warriors/<int:pk>/delete/', WarriorDeleteAPIView.as_view()),
    path('warriors/<int:pk>/update/', WarriorUpdateAPIView.as_view()),
]
