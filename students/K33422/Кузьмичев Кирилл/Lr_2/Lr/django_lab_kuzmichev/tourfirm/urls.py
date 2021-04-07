from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.main),
    path('profile/', views.profile),
    path('myreserves/', listreserves.as_view(), name='reserves'),
    path('myreserves/myreserves/deletereserve/<int:pk>/', views.deletereserveView.as_view()),
    path('myreserves/myreserves/updatereserve/<int:pk>/', views.updatereserveView.as_view()),
    path('register/', register, name='register'),
    path('tours/', views.tourslist),
    path('tours/<int:pk>/reserve/', CreateReserve.as_view(), name='reserve'),
    path('review/', CreateReview.as_view(), name='review'),
    path('soldtours/', views.soldtourslist),
    path('reviews/', views.reviewslist)
 ]
