from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('owner/<int:owner_id>', views.detail, name='detail'),
    path('owner/create', views.CarOwnerCreate.as_view(), name='create'),
    path('cars', views.ListCar.as_view(), name='cars'),
    path('car/<int:car_id>', views.car_detail, name='car_detail'),
    path('car/create', views.AddCar.as_view(), name='add_car'),
    path('car/<int:pk>/update', views.UpdateCar.as_view(), name='update_car'),
    path('car/<int:pk>/delete', views.DeleteCar.as_view(), name='delete_car')
]
