from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('warriors/<int:pk>/', OneWarriorAPIView.as_view()),
    path('warriors/<int:pk>/update/', OneWarriorUpdateAPIView.as_view()),
    path('warriors/list/', WarriorListAPIView.as_view()),
    path('warriors/create/', WarriorCreateAPIView.as_view()),
    path('skills/', GetSkillAPIView.as_view()),
    path('skills/create/', SkillGenericCreateAPIView.as_view()),
    path('skills_of_warrior/create/', SkillOfWarriorCreateAPIView.as_view()),
    path('warriors_skills/list/', WarriorsSkills.as_view()),
    path('profession/create/', ProfessionCreateAPIView.as_view()),
    path('warriors_professions/list/', WarriorsProfession.as_view())

]
