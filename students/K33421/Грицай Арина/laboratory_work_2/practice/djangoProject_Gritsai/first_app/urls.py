from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner),
    path('all_owners/', views.all_owners),
    path('all_vehicles/', views.all_vehicles),
    path('vehicle/<int:pk>/', views.vehicleView.as_view()),
    path('vehicle/<int:pk>/update/', views.upd_vehicleView.as_view()),
    path('vehicle/<int:pk>/delete/', views.del_vehicleView.as_view()),
    path('add_vehicle/', views.add_vehicle.as_view()),
    path('add_owner/', views.add_ownerView)
]
