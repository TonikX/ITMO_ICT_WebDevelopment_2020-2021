from rest_framework import routers

from .api import *

router = routers.DefaultRouter()

router.register('api/hotels', HotelViewSet, 'hotels')
router.register('api/room', RoomViewGet, 'room')
router.register('api/roomSet', RoomViewSet, 'roomSet')
router.register('api/booking', BookingViewGet, 'booking')
router.register('api/bookingSet', BookingViewSet, 'bookingSet')
router.register('api/comments', CommentsViewGet, 'comments')
router.register('api/commentsSet', CommentsViewSet, 'commentsSet')

urlpatterns = router.urls
