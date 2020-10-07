from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),

    path('car_owners/', car_owner_list_view),
    path('car_owners/create/', car_owner_create_view),

    path('cars/', CarListView.as_view()),
    path('car/<int:pk>/', CarDetailView.as_view()),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/create/', CarCreateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
]