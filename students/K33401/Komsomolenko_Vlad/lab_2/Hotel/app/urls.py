from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('mainn/', views.loginPass),
    path('main/', views.Hotels.as_view()),
    path('main/hotel/<int:hotel>/', views.rooms),
    path('room/<int:pk>/', views.RoomDetail.as_view()),
    path('main/hotel/<int:hotel>/feedback/', views.feedback),
    path('feed/<int:pk>/', views.ThisFeedback.as_view()),
    path('add_feed/<int:hotel>/', views.add_feedback),
    path('add_reserve/<int:room>/', views.add_reserve),
    path('my_reserves/', views.myReserves),
    path('my_reserves/reserve/<int:pk>/', views.ThisReserve.as_view()),
    path('my_reserves/reserve/<int:pk>/delete/', views.DeleteReserve.as_view()),
    path('my_reserves/reserve/<int:pk>/update/', views.EditReserve.as_view()),
    path('main/hotel/<int:hotel>/guests/', views.guests),
    path('panel/', views.panel),
    path('panel/edit/<int:pk>/', views.EditPanel.as_view()),
    path('panel_compl/', views.panel_compl),
]
