from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
    # path('warriors/', WarriorAPIView.as_view()),
    path('warriors/', WarriorListAPIView.as_view()),
    path('skills/', SkillAPIView.as_view()),
    path('professions/', ProfessionAPIView.as_view()),
    # path('skill/create/', SkillCreateView.as_view()),
    path('profession/create/', ProfessionCreateAPIView.as_view()),
    # for last part of practice
    # do i need to create warriors with admin panel or rest api?
    path('warrior/create/', WarriorCreateAPIView.as_view()),
    path('skill/create/', SkillCreateAPIView.as_view()),
    # удаление воина по id
    path('warrior/<int:id>/delete', WarriorDestroyAPIView.as_view()),
    # редактирование воина
    path('warrior/<int:pk>/update', WarriorUpdateAPIView.as_view()),
    # просмотр полной информации о воине по id
    path('warrior/<int:pk>', WarriorRetrieveAPIView.as_view()),
    # о воинах и скиллах
    path('warriors_and_skills/', WarriorSkillListAPIView.as_view()),
    # о воинах и профессиях
    path('warriors_and_professions/', WarriorProfessionListAPIView.as_view()),
]
