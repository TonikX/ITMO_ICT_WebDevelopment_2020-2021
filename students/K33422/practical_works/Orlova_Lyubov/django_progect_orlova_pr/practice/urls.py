from django.urls import path
from . import views #подключение файла контроллеров,описанного в пункте 3

urlpatterns = [
    path('owners_list/', views.owners_list),  # Вывод всех владельцев на основе функций
    path('carslist/', views.cars_list.as_view()),  # Вывод всех автомобилей на основе классов
    path('cars_list/<int:pk>/', views.car_detail.as_view()),  # Вывод одного автомобиля по id на основе классов
    path('cars_list/', views.CarListView.as_view()),  # Переопределение стандартных методов в generic view
    path('add_car_owner/', views.add_car_owner),  # Форма добавления владельцев
    path('cars_list/<int:pk>/update/', views.CarUpdate.as_view()),
    path('cars_list/create', views.CarCreate.as_view(success_url="/cars_list/")),
    path('cars_list/<int:pk>/delete/', views.CarDelete.as_view()),
]
