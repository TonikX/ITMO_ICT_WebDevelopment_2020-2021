from django.urls import path
from .views import *

app_name = "app12"

urlpatterns = [
    path('room/list/', RoomListView.as_view()),
    path('room/create/', RoomCreateView.as_view()),
    path('room/<int:pk>/', RoomAllView.as_view()),

    path('staff/list/', StaffListView.as_view()),
    path('staff/create/', StaffCreateView.as_view()),
    path('staff/<int:pk>/', StaffAllView.as_view()),

    path('staff_cleaning/list/', StaffCleaningListView.as_view()),
    path('staff_cleaning/create/', StaffCleaningCreateView.as_view()),
    path('staff_cleaning/<int:pk>/', StaffCleaningAllView.as_view()),

    path('cleaning_params/list/', CleaningParamsListView.as_view()),
    path('cleaning_params/create/', CleaningParamsCreateView.as_view()),
    path('cleaning_params/<int:pk>/', CleaningParamsAllView.as_view()),

    path('guest/list/', GuestListView.as_view()),
    path('guest/create/', GuestCreateView.as_view()),
    path('guest/<int:pk>/', GuestAllView.as_view()),

]