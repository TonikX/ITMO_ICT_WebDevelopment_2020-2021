from django.urls import path
from . import views

urlpatterns = [
    # owners stuff
    path('owners/', views.owners_list),
    path('owners/<int:owner_id>/', views.owner),
    path('owners/create_owner/', views.create_owner),

    # cars stuff
    path('cars/', views.CarListView.as_view()),
    path('cars/create_car/', views.CarCreateView.as_view()),
    path('cars/<int:pk>/', views.CarDetailView.as_view()),
    path('cars/<int:pk>/update/', views.CarUpdateView.as_view()),
    path('cars/<int:pk>/delete/', views.CarDeleteView.as_view()),

]
