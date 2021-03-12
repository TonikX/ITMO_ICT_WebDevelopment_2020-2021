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

    path('warriors/list_p/', Task1.as_view()),
    path('warriors/list_sk/', Task2.as_view()),
    path('warriors/<int:pk>/info/', Task3.as_view()),
    path('warriors/<int:pk>/delete/', Task4.as_view()),
    path('warriors/<int:pk>/update/', Task5.as_view()),
    #path('warriors/<int:pk>/update_skills/', Task5Skills.as_view()),

]