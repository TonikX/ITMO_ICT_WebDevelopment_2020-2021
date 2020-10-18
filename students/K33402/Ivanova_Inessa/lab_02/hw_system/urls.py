from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginFormView.as_view()),
    path('login/', LoginFormView.as_view()),
    path('register/teacher', TeacherRegisterFormView.as_view()),
    path('register/student', StudentRegisterFormView.as_view()),
    path('profile/', LoginPass),
    path('logout/', LogoutView.as_view()),
    
    path('homework/add/', AddHomework.as_view()),
    path('homework/<int:pk>/', HomeworkDetail.as_view(), name='teacher_detail'),
    path('homework/<int:pk>/delete/', DeleteHomework.as_view()),
    path('homeworks/', Homeworks.as_view()),
    path('homework/<int:pk>/<int:ppk>/', AddAssessment.as_view()),
    
    path('to_do/', ToDo.as_view()),
    path('to_do/<int:pk>/', ToDoDetail.as_view()),
    path('to_do/<int:pk>/add_assignment/',AddAssignment.as_view()),
    path('grades/', Statistics.as_view()),
]