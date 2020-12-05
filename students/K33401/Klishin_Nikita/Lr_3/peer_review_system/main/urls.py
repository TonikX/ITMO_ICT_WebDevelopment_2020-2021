from django.contrib import admin
from django.urls import path, include, re_path

from main.views import (
	MyExecutionTaskListView, MyInspectionTaskListView, 
	StudentsClassListView, StudentsClassDetailView,
	TaskListView, TaskDetialView, TaskExecutorsListView, TaskInspectorsListView
)

from accounts.views import (
	StudentListView, StudentDetailView,
)


urlpatterns = [
    path('tasks/', TaskListView.as_view()),
	path('task/<int:pk>/', TaskDetialView.as_view()),
	path('task/<int:pk>/executors/', TaskExecutorsListView.as_view()),
	path('task/<int:pk>/inspectors/', TaskInspectorsListView.as_view()),
	path('my_execution_tasks/', MyExecutionTaskListView.as_view()),
	path('my_inspection_tasks/', MyInspectionTaskListView.as_view()),
	path('students_classes/', StudentsClassListView.as_view()),
	path('students_class/<int:pk>/', StudentsClassDetailView.as_view()),
	path('students/', StudentListView.as_view()),
	path('student/<int:pk>/', StudentDetailView.as_view()),
]