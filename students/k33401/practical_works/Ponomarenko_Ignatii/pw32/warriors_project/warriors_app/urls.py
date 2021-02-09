from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
	path('warriors-and-professions/', WarriorsAndProfessionsAPIView.as_view()),
	path('warriors-and-skills/', WarriorsAndSkillsAPIView.as_view()),
	path('warrior/<int:pk>', WarriorGetAPIView.as_view()),
	path('profession/create/', ProfessionCreateView.as_view()),
	path('skill/create/', SkillCreateView.as_view()),
]