from django.urls import path 
from . import views

urlpatterns = [
    path('owner/<int:owner_id>', views.detail),
    path('owner/list', views.owner_list),
    path('owner/create', views.car_owner_create),

    path('car/<int:pk>', views.CarDetail.as_view()),
    path('car/list', views.CarListView.as_view()),
    path('car/create', views.CarCreate.as_view()),
    path('car/update/<int:pk>', views.CarUpdate.as_view()),
    path('car/delete/<int:pk>', views.CarDelete.as_view()),
]