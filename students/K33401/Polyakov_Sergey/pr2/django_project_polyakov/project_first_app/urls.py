from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexPage.as_view()),
    path('owner/<int:id>/', owner_detail_view),
    path('owners/', owners_list_view),
    path('owner/create/', owner_create_view),
    path('cars/', CarsListView.as_view()),
    path('car/<int:pk>/', CarDetailView.as_view()),
    path('car/create/', CarCreateView.as_view()),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view())
]
