from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),

    path('skill/create/', SkillCreateView.as_view()),
    path('skills/', SkillAPIView.as_view()),

    path('warriors/list/', WarriorListAPIView.as_view()),
    path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
    path('warrior/create/', WarriorCreateAPIView.as_view()),

    path('warriors/profession_list/', WarriorProfessionListAPIView.as_view()),
    path('warriors/skill_list/', WarriorSkillListAPIView.as_view()),
    path('warriors/info/<int:pk>/', WarriorInfoAPIView.as_view()),
    path('warriors/delete/<int:pk>/', WarriorDeleteAPIView.as_view()),
    path('warriors/update/<int:pk>/', WarriorUpdateAPIView.as_view()),

]
