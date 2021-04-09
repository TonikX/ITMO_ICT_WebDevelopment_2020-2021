from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginFormView.as_view()),
    path('register/', RegisterFormView.as_view()),
    path('login/', LoginFormView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', loginPass),

    path('task/', TeacherTask.as_view()),
    path('task/create/', TeacherTaskCreate.as_view()),
    path('task/<int:pk>/', TeacherTaskDetail.as_view(), name='teacher_detail'),
    path('task/<int:pk>/update/', TeacherTaskUpdate.as_view()),
    path('task/<int:pk>/delete/', TeacherTaskDelete.as_view()),
    path('task/<int:pk>/<str:ppk>/', TeacherTaskCheck.as_view()),

    path('pupil_task/', PupilTask.as_view()),
    path('pupil_task/<int:pk>/', PupilTask_detail.as_view()),
    path('pupil_task/<int:pk>/create/', PupilTask_create.as_view()),
    path('marks/', PupilMark.as_view()),

]
