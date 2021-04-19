from django.urls import path
from . import views

urlpatterns = [
    # drivers
    path('drivers/all', views.DriverListAPIView.as_view()),
    path('drivers/add', views.DriverListAPIView.as_view()),
    path('drivers/<int:pk>', views.DriverDetailAPIView.as_view()),
    path('drivers/edit/<int:pk>', views.DriverDetailAPIView.as_view()),
    path('drivers/delete/<int:pk>', views.DriverDetailAPIView.as_view()),

    # buses
    path('buses/all', views.BusListAPIView.as_view()),
    path('buses/add', views.BusListAPIView.as_view()),
    path('buses/<str:pk>', views.BusDetailAPIView.as_view()),
    path('buses/edit/<str:pk>', views.BusDetailAPIView.as_view()),
    path('buses/delete/<str:pk>', views.BusDetailAPIView.as_view()),

    # shifts
    path('shifts/all', views.ShiftsListAPIView.as_view()),
    path('shifts/add', views.ShiftsListAPIView.as_view()),
    path('shifts/<int:pk>', views.ShiftsDetailAPIView.as_view()),
    path('shifts/edit/<int:pk>', views.ShiftsDetailAPIView.as_view()),
    path('shifts/delete/<int:pk>', views.ShiftsDetailAPIView.as_view()),

    # routs
    path('routs/all', views.RoutesListAPIView.as_view()),
    path('routs/add', views.RoutesListAPIView.as_view()),
    path('routs/<int:pk>', views.RoutesDetailAPIView.as_view()),
    path('routs/edit/<int:pk>', views.RoutesDetailAPIView.as_view()),
    path('routs/delete/<int:pk>', views.RoutesDetailAPIView.as_view()),

]

