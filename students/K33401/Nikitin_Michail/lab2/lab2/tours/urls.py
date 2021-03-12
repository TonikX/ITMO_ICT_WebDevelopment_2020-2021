from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from tours import views


urlpatterns = [
    path('', views.StartPage.as_view()),
    path('login/', LoginView.as_view(template_name='login.html')),
    path('logout/', LogoutView.as_view()),
    path('registration/', views.registration),
    path('tour/<int:tour_id>', views.tour_view),
    path('booking/<int:tour_id>', views.booking),
    path('booklist/', views.BookList.as_view()),
    path('bookdel/<int:book_id>', views.booking_del),
    #path('comment/<int:tour_id>', views.RetryCommenting.as_view()),
    path('comment/<int:tour_id>', views.users_comment),
    path('comment/all', views.CommentList.as_view())
]
