from django.urls import path

from .views import CarDetailView, get_owners, get_owner, owner_create_view, CarList, CarCreateView, CarUpdateView, CarRemoveView


urlpatterns = [
    path('owners/', get_owners),
    path('owner/<int:id>/', get_owner),
    path('owners/create', owner_create_view),
    path('cars/', CarList.as_view()),
    path('car/<int:pk>', CarDetailView.as_view()),
    path('cars/create', CarCreateView.as_view()),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/<int:pk>/remove/', CarRemoveView.as_view())
]

