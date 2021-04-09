from rest_framework import routers

from .api import *

router = routers.DefaultRouter()

router.register('api/airlines', AirlinesViewSet, 'airlines')
router.register('api/cityAirport', CityAirportViewSet, 'cityAirport')
router.register('api/flight', FlightViewSet, 'flight')
router.register('api/flightGet', FlightViewGet, 'flightGet')
router.register('api/place', PlaceViewSet, 'place')
router.register('api/placeGet', PlaceViewGet, 'placeGet')
router.register('api/comments', CommentsViewSet, 'comments')

urlpatterns = router.urls
