from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home),
    path('climbers/create', ClimberCreateAPIView.as_view(),
         name='create_climber_url'),
    path('climbers/<int:pk>', ClimberRetrieveUpdateAPIView.as_view(),
         name='update_climber_url'),
    path('peaks/create', PeakCreateAPIView.as_view(), name='create_peak_url'),
    path('peaks/<int:pk>', PeakRetrieveUpdateAPIView.as_view(),
         name='update_peak_url'),
    path('climbings/create', ClimbingCreateAPIView.as_view(),
         name='create_climbing_url'),
    path('participations/create',
         ParticipationCreateAPIView.as_view(), name='create_participation_url'),
    path('emergencies/create',
         EmergencySituationCreateAPIView.as_view(), name='create_emergency_situation_url'),
    #
    path('climbers/', ClimberClimbingListAPIView.as_view()),
    path('climbings/', FromToClimbingListAPIView.as_view()),
    path('peaks/<int:pk>/unique_climbers', ClimbersOnPeakListAPIView.as_view(),
         name='climbers_on_peak_url'),
    path('peaks/no_climbings', PeakWithoutClimbingListAPIView.as_view(),
         name='peaks_no_climbings_url'),
    path('peaks/<int:pk>/climber_count', CountClimbersOnPeakListAPIView.as_view(),
         name='count_climbers_on_peak_url'),
    # for 4 lab
    path('peaks/', PeakListAPIView.as_view()),
    path('clubs/', ClubListAPIView.as_view()),
    path('participations/', ParticipationListAPIView.as_view()),
    path('', redirect_home)
]
