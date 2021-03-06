from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
    path('warriors/list/', WarriorListAPIView.as_view()),
    path('warriors/prof/', ProfessionAPIView.as_view()),
    path('warriors/skills/', SkillOfWarriorAPIView.as_view()),
    path('skills/', SkillAPIView.as_view()),
    path('skills/create/', SkillCreateView.as_view()),
    path('warriors/<int:pk>', SingleWarriorAPIView.as_view()),
    path('warriors/delete/<int:pk>', WarriorDestroyView.as_view()),
    path('warriors/update/<int:pk>', WarriorUpdateView.as_view()),
    path('warriors/skills/update/<int:pk>', SkillOfWarriorUpdateView.as_view()),
]
