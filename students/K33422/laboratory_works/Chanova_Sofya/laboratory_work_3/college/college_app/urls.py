from django.urls import path
from .views import *

app_name = "college_app"


urlpatterns = [
    path('profile/<str:username>', UserProfileAPIView.as_view()),
    path('profile/<str:username>/edit', EditUserAPIView.as_view()),

    path('students/', StudentsListAPIView.as_view()),
    path('teachers/', TeachersListAPIView.as_view()),
    path('staff/', StaffListAPIView.as_view()),

    path('schedule/', ScheduleListAPIView.as_view()),
    path('schedule/add/', ScheduleEntryCreateAPIView.as_view()),
    path('schedule/<int:pk>/', ScheduleEntryPageAPIView.as_view()),
    path('schedule/mine/', MyScheduleListAPIView.as_view()),

    path('groups/', StudentGroupsListAPIView.as_view()),
    path('groups/add/', StudentGroupCreateAPIView.as_view()),
    path('groups/<int:pk>/', StudentGroupPageAPIView.as_view()),

    path('subjects/', SubjectsListAPIView.as_view()),
    path('subjects/add/', SubjectCreateAPIView.as_view()),
    path('subjects/<int:pk>/', SubjectPageAPIView.as_view()),

    path('rooms/', RoomsListAPIView.as_view()),
    path('rooms/add/', RoomCreateAPIView.as_view()),
    path('rooms/<int:pk>/', RoomPageAPIView.as_view()),

    path('grades/', SemesterGradesListAPIView.as_view()),
    path('grades/add/', SemesterGradeCreateAPIView.as_view()),
    path('grades/<int:pk>/', SemesterGradePageAPIView.as_view()),

    path('teachings/', TeachingsListAPIView.as_view()),
    path('teachings/add/', TeachingCreateAPIView.as_view()),
    path('teachings/<int:pk>/', TeachingPageAPIView.as_view()),

]