from django.urls import path

from polls_app.views import PollsAPIView, PollCreateAPIView, PollAPIView, PollUpdateAPIView, PollDeleteAPIView, \
    UserToAnswerCreateAPIView, StatisticAPIView

urlpatterns = [
    path('polls/', PollsAPIView.as_view()),
    path('polls/create/', PollCreateAPIView.as_view()),
    path('polls/<int:pk>/', PollAPIView.as_view()),
    path('polls/statistic/', StatisticAPIView.as_view()),
    path('polls/<int:pk>/update/', PollUpdateAPIView.as_view()),
    path('polls/<int:pk>/delete/', PollDeleteAPIView.as_view()),
    path('user_to_answer/create/', UserToAnswerCreateAPIView.as_view()),
]
