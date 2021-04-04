from django.urls import path
from .views import *


urlpatterns = [
    path('main/', LoginFormView.as_view(), name='main'),
    path('profile/', profile, name='profile'),
    path('registration/', registration, name='registration'),
    path('add_race_registration/', addrace, name='addrace'),
    path('race_registrations/', Registrations, name='registrations'),
    path('races/', races, name='races'),
    path('results/', results, name='results'),
    path('forum/', forum, name='forum'),

]
