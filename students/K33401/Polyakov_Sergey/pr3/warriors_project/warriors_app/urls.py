from django.urls import path
from .views import *

app_name = 'warrior_app'

urlpatterns = [
    path('warriors/', WarriorListAPIView.as_view()),
    path('warriors/<int:pk>/', OneWarriorAPIView.as_view()),
    path('warriors/<int:pk>/update/', OneWarriorUpdateAPIView.as_view()),
    path('warriors/<int:pk>/destroy/', OneWarriorDestroyAPIView.as_view()),
    path('warriors/create/', WarriorCreateAPIView.as_view()),
    path('skills/', GetSkillAPIView.as_view()),
    path('warriors_skills/', WarriorsSkills.as_view()),
    path('warriors_professions/', WarriorsProfession.as_view())
]
